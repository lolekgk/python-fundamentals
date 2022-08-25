from abc import ABC, abstractmethod


class IEmailBuilder(ABC):
    @abstractmethod
    def set_from_(self, value: str):
        pass

    @abstractmethod
    def set_to(self, value: str):
        pass

    @abstractmethod
    def set_title(self, value: str):
        pass

    @abstractmethod
    def set_cc(self, value: list):
        pass

    @abstractmethod
    def set_bcc(self, value: list):
        pass

    @abstractmethod
    def set_html(self, value: str):
        pass


class EmailBuilder(IEmailBuilder):
    def __init__(self):
        self.email = Email()

    def set_from_(self, value):
        self.email.from_ = value
        return self

    def set_to(self, value):
        self.email.to = value
        return self

    def set_title(self, value):
        self.email.title = value
        return self

    def set_cc(self, value):
        self.email.cc = value
        return self

    def set_bcc(self, value):
        self.email.bcc = value
        return self

    def set_html(self, value):
        self.email.html = value
        return self

    def get_result(self):
        return self.email


class Email:
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
