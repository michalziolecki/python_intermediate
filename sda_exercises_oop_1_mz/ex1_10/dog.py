from sda_exercises_oop_1_mz.canidae import Canidae
from sda_exercises_oop_1_mz.ex1_10.animal import Animal
from sda_exercises_oop_1_mz.mammal import Mammal


class Dog(Animal, Mammal, Canidae):

    def __init__(self, name):
        super().__init__(name)  # jesli dziedziczymy i klasa Ojciec ma to pole to przekazujemy przez super
        # self. name = name # jesli nie dziedziczymy to wyglada to tak

    def make_sound(self) -> str:
        return f'{self.name} - Hau'

