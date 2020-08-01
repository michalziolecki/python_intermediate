from .abc_figure import Figure
from math import pi as PI


class Rectangle(Figure):

    def __init__(self, high: float, width: float):
        self.high = high
        self.width = width

    def get_area(self) -> float:
        return self.high * self.width


class Circle(Figure):

    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return PI * self.radius ** 2


class Triangle(Figure):

    def __init__(self, high: float, base: float):
        self.high = high
        self.base = base

    def get_area(self) -> float:
        return (self.high * self.base)/2.0
