from decimal import Decimal

from sda_exercises_oop_3_mz.order_item import OrderItem


class Order:

    def __init__(self, list_of_items=None):
        if list_of_items is None:
            list_of_items = []
        self.list_of_items = list_of_items

    def add_item(self, item: OrderItem):
        self.list_of_items.append(item)

    def get_value(self):
        sum = Decimal(0)
        for item in self.list_of_items:
            sum += item
        return sum

    def get_items_count(self) -> int:
        return len(self.list_of_items)

    def show(self):
        print('---Order---')
        for item in self.list_of_items:
            print(item)

