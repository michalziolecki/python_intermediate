from datetime import date


class Person:

    def __init__(self, name: str, surname: str, birthday: date):
        self._name = name
        self._surname = surname
        self._birthday = birthday

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value: str):
        self._surname = value

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value: date):
        self._birthday = value
