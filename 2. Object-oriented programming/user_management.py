from __future__ import annotations

import uuid
from abc import ABC
from datetime import date, datetime
from enum import Enum
from functools import total_ordering
from typing import Union


class RequiredPermissionLvl(Enum):
    EDIT_POST = 5
    DELETE_POST = 6
    SET_ALL_ATTRIBUTES = 6
    CHANGE_PERMISSION_LVL = 6


class PermissionLvl(Enum):
    USER = 1
    REDACTOR = 5
    ADMIN = 10


class PermissionError(Exception):
    def __init__(self):
        default_message = "You do not have permission to do this."
        super().__init__(default_message)


class AbstractUser(ABC):
    permission_lvl = PermissionLvl.USER.value

    def __init__(
        self,
        name: str,
        surname: str,
        email: str,
        birth_date: date,
        gender: str,
    ):
        self._id = uuid.uuid4()
        self._posts = {}
        self._name = name
        self._surname = surname
        self._email = email
        self._birth_date = birth_date
        self._gender = gender

    def __eq__(self, other) -> bool:
        if self.__class__ == other.__class__:
            return (self._name + self._surname) == (
                other._name + other._surname
            )
        return False

    def __hash__(self) -> int:
        return hash(self._id)

    def __gt__(self, other) -> bool:
        return self.permission_lvl > other.permission_lvl

    def __lt__(self, other) -> bool:
        return self.permission_lvl < other.permission_lvl

    @property
    def name(self) -> str:
        return self._name

    @property
    def surname(self) -> str:
        return self._surname

    @property
    def email(self) -> str:
        return self._email

    @property
    def birth_date(self) -> date:
        return self._birth_date

    @property
    def gender(self) -> str:
        return self._gender

    def change_permission_lvl(
        self, user: AbstractUser, new_permission_lvl: int
    ):
        if self == user:
            raise PermissionError(
                'You can not change your own permission_lvl.'
            )
        if (
            self.permission_lvl
            >= RequiredPermissionLvl.CHANGE_PERMISSION_LVL.value
        ):
            self.permission_lvl = new_permission_lvl
        else:
            raise PermissionError

    def change_attribute(
        self, name: str, value: Union[str, date, uuid.UUID], user: AbstractUser
    ):
        if (
            f'_{name}' in user.__dict__
            and self.permission_lvl
            >= RequiredPermissionLvl.SET_ALL_ATTRIBUTES.value
        ) or (self == user and name == 'email'):
            setattr(user, f'_{name}', value)
        else:
            raise PermissionError

    def add_post(self, content: str) -> Post:
        post = Post(content, author=self)
        self._posts[post._id] = post
        return post

    def edit_post(self, post: Post, new_content: str):
        if (
            post.author == self
            or self.permission_lvl >= RequiredPermissionLvl.EDIT_POST.value
        ):
            post.content = new_content
        else:
            raise PermissionError

    def delete_post(self, post: Post):
        if (
            post.author == self
            or self.permission_lvl >= RequiredPermissionLvl.DELETE_POST.value
        ):
            del post.author._posts[post._id], post
        else:
            raise PermissionError


class User(AbstractUser):
    pass


class Admin(AbstractUser):
    permission_lvl = PermissionLvl.ADMIN.value


class Redactor(AbstractUser):
    permission_lvl = PermissionLvl.REDACTOR.value


@total_ordering
class Post:
    comparsion_error_str = (
        "Comparsion is not supported between instances of {} and {}."
    )

    def __init__(self, content: str, author: AbstractUser):
        self._id = uuid.uuid4()
        self.content = content
        self._author = author
        self._creation_date = datetime.now()

    def __eq__(self, other) -> bool:
        if isinstance(other, Post):
            return len(self.content) == len(other.content)
        raise TypeError(
            self.comparsion_error_str.format(
                self.__class__.__name__, other.__class__.__name__
            ),
        )

    def __lt__(self, other) -> bool:
        if isinstance(other, Post):
            return len(self.content) < len(other.content)
        raise TypeError(
            self.comparsion_error_str.format(
                self.__class__.__name__, other.__class__.__name__
            ),
        )

    @property
    def author(self) -> AbstractUser:
        return self._author

    @property
    def content(self) -> str:
        return self._content

    @property
    def creation_date(self) -> datetime:
        return self._creation_date

    @property
    def modification_date(self) -> datetime:
        return self._modification_date

    @content.setter
    def content(self, value: str):
        self._content = value
        self._modification_date = datetime.now()


user = User('Karol', 'Gajda', 'karol.gajda97@gmail.com', '21', 'male')
user2 = User('Karol', 'Gajda', 'karol.gajda97@gmail.com', '21', 'male')
red = Redactor('Karol', 'Gajda', 'karol.gajda97@gmail.com', '21', 'male')
red2 = Redactor('Karol', 'Gajda', 'karol.gajda97@gmail.com', '21', 'male')

admin = Admin('Karol', 'Gajda', 'admin', 'admin', 'admin')
post = user.add_post('blalala')
post2 = admin.add_post('blalla')
# print(user < admin)
# print(user < red)
# print(hash(user))
# print(hash(user2))
# print(admin.__class__)
# d = {red: 1}
# print(d)
# print(post <= user)
user.change_permission_lvl(user, 20)
print(Admin.permission_lvl)
print(admin.permission_lvl)
