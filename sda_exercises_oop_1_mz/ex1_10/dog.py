from sda_exercises_oop_1_mz.ex1_10.animal import Animal


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)  # jesli dziedziczymy i klasa Ojciec ma to pole to przekazujemy przez super
        # self. name = name # jesli nie dziedziczymy to wyglada to tak

    def make_sound(self) -> str:
        return f'{self.name} - Hau'

