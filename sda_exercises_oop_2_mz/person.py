from datetime import date
from enum import Enum


class Sex(Enum):
    MALE = 1
    FEMALE = 2


class Person:

    def __init__(self, name: str, surname: str, birthday: date, sex=Sex.MALE):
        self._name = name
        self._surname = surname
        self._birthday = birthday
        self._sex = sex

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value: Sex):
        self._sex = value

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
