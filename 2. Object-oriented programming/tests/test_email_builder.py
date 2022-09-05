import pytest
from email_builder import Email, EmailBuilder


@pytest.fixture
def builder():
    builder = EmailBuilder()
    yield builder
    del builder


class TestEmailBuilder:
    def test_email_builder_attribute_is_an_email_instance(self, builder):
        assert isinstance(builder.email, Email)

    def test_add_attribute_that_is_allowed(self, builder):
        builder.add_attribute('title', 'Hello')
        assert builder.email.title == 'Hello'
        assert builder.email.from_ == ''
        assert builder.email.to == ''
        assert builder.email.cc is None
        assert builder.email.bcc is None
        assert builder.email.html == ''

    def test_add_attribute_that_is_not_allowed(self, builder):
        with pytest.raises(AttributeError):
            builder.add_attribute('footer', 'Bye')

    def test_add_some_part_of_the_allowed_attributes(self, builder):
        builder.add_attribute('from_', 'test@gmail.com')
        builder.add_attribute('to', 'test2@gmail.com')
        builder.add_attribute('title', 'I have a question.')
        assert builder.email.from_ == 'test@gmail.com'
        assert builder.email.to == 'test2@gmail.com'
        assert builder.email.title == 'I have a question.'
        assert builder.email.cc is None
        assert builder.email.bcc is None
        assert builder.email.html == ''

    def test_all_allowed_attributes(self, builder):
        builder.add_attribute('from_', 'test@gmail.com')
        builder.add_attribute('to', 'test2@gmail.com')
        builder.add_attribute('title', 'I have a question.')
        builder.add_attribute('cc', ['test3@gmail.com', 'test4@gmail.com'])
        builder.add_attribute('bcc', ['test5@gmail.com', 'test6@gmail.com'])
        builder.add_attribute('html', 'test')
        assert builder.email.from_ == 'test@gmail.com'
        assert builder.email.to == 'test2@gmail.com'
        assert builder.email.title == 'I have a question.'
        assert builder.email.cc == ['test3@gmail.com', 'test4@gmail.com']
        assert builder.email.bcc == ['test5@gmail.com', 'test6@gmail.com']
        assert builder.email.html == 'test'
