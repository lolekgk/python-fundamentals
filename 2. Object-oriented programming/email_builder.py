from abc import ABC, abstractmethod
from typing import Union


class IEmailBuilder(ABC):
    @abstractmethod
    def add_attribute(self, name: str, value: Union[str, list]):
        pass


class EmailBuilder(IEmailBuilder):
    def __init__(self):
        self.email = Email()

    def add_attribute(self, name, value):
        setattr(self.email, name, value)
        return self

    def get_result(self):
        return self.email


class Email:
    __slots__ = ('from_', 'to', 'title', 'cc', 'bcc', 'html')

    def __init__(self, from_="", to="", title="", cc=None, bcc=None, html=""):
        self.from_ = from_
        self.to = to
        self.title = title
        self.cc = cc
        self.bcc = bcc
        self.html = html

    def __str__(self):
        return (
            f"{15 * '='}New Message{15 * '='}\n"
            f"From: {self.from_}\n"
            f"To: {self.to}\n"
            f"Title: {self.title}\n"
            f"CC: {self.cc}\n"
            f"BCC: {self.bcc}\n"
            f"{self.html}"
        )
