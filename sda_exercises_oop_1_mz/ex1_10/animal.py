from abc import ABC


class Animal(ABC):

    def __init__(self, name):
        self._name = name  # pole proteced czyli dostepne w drodze dziedziczenia

    @property
    def name(self) -> str:
        return self._name
