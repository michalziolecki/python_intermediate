from decimal import Decimal  # jest to typ o duzej i ustalonej precyzji dla walut

from sda_exercises_oop_3_mz.order_item_error import OrderItemError


class OrderItem:

    def __init__(self, name: str, number: int, price: Decimal):
        self.name = name
        self.number = number
        self.price = price
        self.all_price: Decimal = self.number * self.price

    def get_value(self) -> Decimal:
        if not self.is_correct():
            raise OrderItemError('Price for order equal or below zero!')
        return self.all_price

    def is_correct(self) -> bool:
        if self.all_price <= Decimal(0):
            return False
        return True

    def show(self) -> None:
        print(f'{self.name} {self.price} {self.number} szt {self.price} zł')

    def __str__(self) -> str:
        return f'{self.name} {self.price} {self.number} szt {self.price} zł'
