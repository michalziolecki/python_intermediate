class MyIterable:

    def __init__(self, amount):
        self.amount = amount
        self.values_created = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.values_created >= self.amount - 1:
            raise StopIteration
        self.values_created += 1
        return self.values_created
