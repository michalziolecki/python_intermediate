from datetime import date

from sda_exercises_oop_2_mz.employee import Employee


class Manager(Employee):

    def __init__(self, name: str, surname: str, birthday: date, salary=1000.0):
        salary = salary * 1.1
        super().__init__(name, surname, birthday, salary)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        self._salary = value * 1.1

    def who_am_i(self):
        print(f'Nazywam sie manager {self.name} {self.surname} i zarabiam {self.salary} zł')
