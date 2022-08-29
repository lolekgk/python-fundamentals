from __future__ import annotations

import uuid
from abc import ABC
from datetime import date, datetime
from enum import Enum
from typing import Union


class RequiredPermissionLvl(Enum):
    EDIT_POST = 5
    DELETE_POST = 6
    SET_ALL_ATTRIBUTES = 6


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


class Post:
    def __init__(self, content: str, author: AbstractUser):
        self._id = uuid.uuid4()
        self.content = content
        self._author = author
        self._creation_date = datetime.now()

    @property
    def author(self) -> AbstractUser:
        return self._author

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value: str):
        self._content = value
        self.modification_date = datetime.now()
