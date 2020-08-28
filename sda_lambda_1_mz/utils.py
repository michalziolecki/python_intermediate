from decimal import Decimal
from random import randint


def list_sorting_ex1():
    names = ['Marian', 'Kamil', 'Ala', 'Maciej', 'Krystian', '']
    # a
    print('a. result:')
    print(sorted(names, key=lambda name: len(name)))
    # b
    print('b. result:')
    print(sorted(names, key=lambda name: len(name), reverse=True))
    # c
    print('c. result:')
    print(sorted(names, key=lambda name: name[0] if len(name) > 0 else ''))


class BankAccount:
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name} - {self.balance}'


def lambda_ex2_and_ex3():
    account1 = BankAccount('1', Decimal(1000))
    account2 = BankAccount('2', Decimal(4000))
    account3 = BankAccount('3', Decimal(5000))
    account4 = BankAccount('4', Decimal(7000))
    account5 = BankAccount('5', Decimal(10000))

    accounts = [account1, account2, account3, account4, account5]

    # ex2
    print('ex2')
    filtered_accounts = list(filter(lambda account: account if account.balance > Decimal(4500) else None, accounts))
    for account in filtered_accounts:
        print(account)

    # ex3
    print('ex3:')
    max_account = max(accounts, key=lambda account: account.balance)
    print(max_account)


def ex4_lambda():
    randoms = [randint(0, 101) for item in range(10)]
    print('before: ')
    print(randoms)
    print('after: ')
    print(list(map(lambda number: 2 * number, randoms)))


def ex5_lambda():
    randoms = [randint(100, 200) for item in range(10)]
    print('before: ')
    print(randoms)
    print('after - from min to max: ')
    print(list(sorted(randoms)))
    print('after - from max to min: ')
    print(list(sorted(randoms, reverse=True)))
