from datetime import date, datetime

import pytest
from user_management import Admin, PermissionError, Post, Redactor, User


@pytest.fixture
def test_user():
    user = User(
        'Bukayo', 'Saka', 'bukayo@gmail.com', date(2001, 12, 10), 'male'
    )
    yield user
    del user


@pytest.fixture
def test_users_post(test_user):
    post = test_user.add_post('Post content')
    yield post
    test_user._posts.pop(post._id, None)
    del post


@pytest.fixture
def test_user_clone():
    user = User(
        'Bukayo', 'Saka', 'bukayo22@gmail.com', date(2001, 12, 10), 'male'
    )
    yield user
    del user


@pytest.fixture
def second_test_user():
    user = User(
        'Adama', 'Traore', 'adama@gmail.com', date(2011, 11, 30), 'male'
    )
    yield user
    del user


@pytest.fixture
def test_redactor():
    redactor = Redactor(
        'Bukayo', 'Saka', 'bukayo22@gmail.com', date(2001, 12, 10), 'male'
    )
    yield redactor
    del redactor


@pytest.fixture
def test_redactors_post(test_redactor):
    post = test_redactor.add_post('Post content')
    yield post
    test_redactor._posts.pop(post._id, None)
    del post


@pytest.fixture
def test_admin():
    admin = Admin(
        'Mikel', 'Arteta', 'mikelarteta@gmail.com', date(1980, 10, 20), 'male'
    )
    yield admin
    del admin


class TestUser:
    def test_the_same_user_classes_with_the_same_name_and_surname_comparssion(
        self, test_user, test_user_clone
    ):
        assert test_user == test_user_clone

    def test_different_user_classes_with_the_same_name_and_surname_comparssion(
        self, test_user, test_redactor
    ):
        assert test_user != test_redactor

    def test_the_same_user_classes_with_different_name_and_surname_comparssion(
        self, test_user, second_test_user
    ):
        assert test_user != second_test_user

    def test_different_user_classes_with_different_names(
        self, test_user, test_admin
    ):
        assert test_user != test_admin

    def test_user_can_add_post(self, test_user, test_users_post):
        assert test_users_post.author == test_user
        assert test_users_post.content == 'Post content'
        assert len(test_user._posts) == 1

    def test_user_can_edit_his_own_post(self, test_user, test_users_post):
        test_user.edit_post(test_users_post, 'New content')
        assert test_users_post.content == 'New content'

    def test_user_can_not_edit_other_users_posts(
        self, test_user, test_redactors_post
    ):
        with pytest.raises(PermissionError):
            test_user.edit_post(test_redactors_post, 'New content')

    def test_user_can_delete_his_own_post(self, test_user, test_users_post):
        assert len(test_user._posts) == 1
        test_user.delete_post(test_users_post)
        assert len(test_user._posts) == 0

    def test_user_can_not_delete_other_users_post(
        self, test_user, test_redactors_post
    ):
        with pytest.raises(PermissionError):
            test_user.delete_post(test_redactors_post)

    def test_user_can_change_his_own_email(self, test_user):
        test_user.change_attribute('email', 'new.email@gmail.com', test_user)
        assert test_user.email == 'new.email@gmail.com'

    def test_user_can_not_change_name(self, test_user):
        with pytest.raises(PermissionError):
            test_user.change_attribute('name', 'Bob', test_user)

    def test_user_can_not_change_own_surnname(self, test_user):
        with pytest.raises(PermissionError):
            test_user.change_attribute('surname', 'Marley', test_user)

    def test_user_can_not_change_own_birth_date(self, test_user):
        with pytest.raises(PermissionError):
            test_user.change_attribute(
                'birth_date', date(2020, 1, 2), test_user
            )

    def test_user_can_not_change_own_gender(self, test_user):
        with pytest.raises(PermissionError):
            test_user.change_attribute('gender', 'female', test_user)

    def test_user_can_not_set_own_new_attribute(self, test_user):
        with pytest.raises(PermissionError):
            test_user.change_attribute('second_name', 'Francis', test_user)

    def test_user_can_not_change_others_attributes(
        self, test_user, second_test_user
    ):
        with pytest.raises(PermissionError):
            test_user.change_attribute('gender', 'female', second_test_user)

    def test_compare_different_user_classes(
        self, test_user, test_redactor, test_admin
    ):
        assert test_user < test_redactor < test_admin

    def test_user_class_can_be_dict_key(self, test_user):
        test_dict = {test_user: 1}
        assert test_dict[test_user] == 1
        del test_dict


class TestRedactor:
    def test_redactor_can_add_post(self, test_redactor, test_redactors_post):
        assert test_redactors_post.author == test_redactor
        assert test_redactors_post.content == 'Post content'
        assert len(test_redactor._posts) == 1

    def test_redactor_can_edit_his_own_post(
        self, test_redactor, test_redactors_post
    ):
        test_redactor.edit_post(test_redactors_post, 'New content')
        assert test_redactors_post.content == 'New content'

    def test_redactor_can_edit_other_users_posts(
        self, test_redactor, test_users_post
    ):
        test_redactor.edit_post(test_users_post, 'New content')
        assert test_users_post.content == 'New content'

    def test_redactor_can_delete_his_own_post(
        self, test_redactor, test_redactors_post
    ):
        assert len(test_redactor._posts) == 1
        test_redactor.delete_post(test_redactors_post)
        assert len(test_redactor._posts) == 0

    def test_redactor_can_not_delete_other_users_post(
        self, test_redactor, test_users_post
    ):
        with pytest.raises(PermissionError):
            test_redactor.delete_post(test_users_post)

    def test_redactor_can_change_his_own_email(self, test_redactor):
        test_redactor.change_attribute(
            'email', 'new.email@gmail.com', test_redactor
        )
        assert test_redactor.email == 'new.email@gmail.com'

    def test_redactor_can_not_change_name(self, test_redactor):
        with pytest.raises(PermissionError):
            test_redactor.change_attribute('name', 'Bob', test_redactor)

    def test_redactor_can_not_change_own_surnname(self, test_redactor):
        with pytest.raises(PermissionError):
            test_redactor.change_attribute('surname', 'Marley', test_redactor)

    def test_redactor_can_not_change_own_birth_date(self, test_redactor):
        with pytest.raises(PermissionError):
            test_redactor.change_attribute(
                'birth_date', date(2020, 1, 2), test_redactor
            )

    def test_redactor_can_not_change_own_gender(self, test_redactor):
        with pytest.raises(PermissionError):
            test_redactor.change_attribute('gender', 'female', test_redactor)

    def test_redactor_can_not_set_own_new_attribute(self, test_redactor):
        with pytest.raises(PermissionError):
            test_redactor.change_attribute(
                'second_name', 'Francis', test_redactor
            )

    def test_redactor_can_not_change_others_attributes(
        self, test_redactor, second_test_user
    ):
        with pytest.raises(PermissionError):
            test_redactor.change_attribute(
                'gender', 'female', second_test_user
            )

    def test_redactor_class_can_be_dict_key(self, test_redactor):
        test_dict = {test_redactor: 1}
        assert test_dict[test_redactor] == 1
        del test_dict
