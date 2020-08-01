from sda_exceptions_1_mz.exercises_1_mz import ex1

from datetime import date
from sda_exercises_oop_2_mz.employee import Employee
from sda_exercises_oop_2_mz.manager import Manager
from sda_exercises_oop_1_mz.ex1_10.cat import Cat
from sda_exercises_oop_1_mz.ex1_10.dog import Dog

# zwrocenie wartosci przez przypisanie - return
from sda_exercises_oop_3_mz.complex import MyComplex
from sda_exercises_oop_3_mz.order import Order
from sda_exercises_oop_3_mz.order_item import *


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
    # cats = ex2()
    # cat = Cat('aaa')
    # cat.eat_mouse()
    # cat.eat_mouse()
    # animals = []
    # print('adres list: ' + hex(id(animals)))
    # ex5(animals)
    # print('adres list: ' + hex(id(animals)))
    # for animal in animals:
    #     print(animal.make_sound())
    #
    # # ex 7
    # cat.move()
    #
    # #ex 11-13
    #
    # #blok sda2
    # manager = Manager('Jan', 'Kowalski', date(1992, 10, 10), 4500)
    # print(manager.salary)
    # manager.who_am_i()
    #
    # employee = Employee('Jan', 'Kowalski', date(1992, 10, 10), 2500)
    # print(employee.salary)
    # employee.who_am_i()

    # 3_mz
    # number1 = MyComplex(100, 20)
    # number1.show()
    # print(number1)
    #
    # number2 = MyComplex(100, 20)
    # number2.show()
    # print(number2)
    #
    # number3 = MyComplex(101, 20)
    # number3.show()
    # print(number3)
    #
    # print(f'compare complex: {number2.is_equal_to(100, 20)}')
    # print(f'compare complex: {number1==number2}')
    # print(f'compare complex: {number2==number3}')
    #
    # complex_list = [number1, number2, number3]
    #
    # print(MyComplex.add_two_complex(number1, number2))
    # print(MyComplex.add_three_complex(number1, number2, number3))
    # print(MyComplex.add_many_complex(complex_list))
    #
    # print(number1.add(number2))
    item1 = OrderItem('Ser', 3, Decimal(4.50))
    item1.show()
    print(item1)
    print(item1.is_correct())

    item2 = OrderItem('Masło', 0, Decimal(6.50))
    item2.show()
    print(item2)
    try:
        print(item2.get_value())
    except ValueError as ve:
        print(f'Error cached {ve.args}')
    print(item2.is_correct())

    item3 = OrderItem('Musztarda', 2, Decimal(2.50))
    item3.show()

    order = Order()
    order.add_item(item1)
    order.add_item(item3)
    order.show()

    # exceptions
    ex1()


if __name__ == "__main__":
    main()
