from sda_exercises_oop_1_mz.ex1_10.animal import Animal
from sda_exercises_oop_1_mz.ex1_10.moveable import Movable


class Cat(Animal, Movable):

    def __init__(self, name: str):
        super().__init__(name)  # jesli dziedziczymy i klasa Ojciec ma to pole to przekazujemy przez super
        # self.__name: str = name # jesli nie dziedziczymy to wyglada to tak
        self.__eat: int = 0

    @property
    def eat(self) -> int:
        return self.__eat

    @eat.setter
    def eat(self, val):
        self.__eat = val

    def make_sound(self) -> str:
        return f'{self.name} - Mrau'

    def eat_mouse(self):
        self.eat = self.eat + 1
        print(f'Zjadłem mysz: {self.eat}')

    def move(self):
        print('ide')
