import re


def regex_ex1():
    print('Write number')
    value = input()
    expression = '[0-9]+'
    if re.match(expression, value):
        if int(value) % 2 == 0:
            print('even number')
        else:
            print('odd number')
    else:
        print('Incorrect number')


def regex_ex2():
    print('Write postal code')
    value = input()
    expression = '[0-9]{2}-[0-9]{3}'
    if re.match(expression, value):
        print('correct postal code')
    else:
        print('Incorrect postal code')


def regex_ex3():
    print('Write login')
    value = input()
    expression = '[0-9a-zA-Z]{8,16}'
    if re.match(expression, value):
        print('correct login')
    else:
        print('Incorrect login')


def regex_ex4():
    print('Write something with ala')
    value = input()
    expression = '.*ala.*'
    if re.match(expression, value):
        print('ala found')
    else:
        print('ala not found')


def regex_ex5():
    print('Write date')
    value = input()
    expression = '([0-9]{2}\.){2}[0-9]{4}r\.'
    if re.match(expression, value):
        print('date found')
    else:
        print('date not found')


def regex_ex6():
    pass


def regex_ex7():
    pass


def regex_ex8():
    pass


def regex_ex9():
    pass
