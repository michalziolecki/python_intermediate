from datetime import date
from sda_exercises_oop_2_mz.employee import Employee
from sda_exercises_oop_2_mz.manager import Manager
from sda_exercises_oop_1_mz.ex1_10.cat import Cat
from sda_exercises_oop_1_mz.ex1_10.dog import Dog


# zwrocenie wartosci przez przypisanie - return
def ex2() -> list:
    cats = []
    cat1 = Cat('Antek')
    cat2 = Cat('Majtek')
    cat3 = Cat('Kajtek')
    cats.append(cat1)
    cats.append(cat2)
    cats.append(cat3)
    return cats


# przekazanie przez referencje - jako argument
def ex5(animals: list):
    cat1 = Cat('Antek')
    cat2 = Cat('Majtek')
    cat3 = Cat('Kajtek')
    dog1 = Dog('Batory')
    dog2 = Dog('Felix')
    animals.append(cat1)
    animals.append(cat2)
    animals.append(cat3)
    animals.append(dog1)
    animals.append(dog2)


def main():
    cats = ex2()
    cat = Cat('aaa')
    cat.eat_mouse()
    cat.eat_mouse()
    animals = []
    print('adres list: ' + hex(id(animals)))
    ex5(animals)
    print('adres list: ' + hex(id(animals)))
    for animal in animals:
        print(animal.make_sound())

    # ex 7
    cat.move()

    #ex 11-13

    #blok sda2
    manager = Manager('Jan', 'Kowalski', date(1992, 10, 10), 4500)
    print(manager.salary)
    manager.who_am_i()

    employee = Employee('Jan', 'Kowalski', date(1992, 10, 10), 2500)
    print(employee.salary)
    employee.who_am_i()



if __name__ == "__main__":
    main()
