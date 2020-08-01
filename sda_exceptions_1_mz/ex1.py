def ex1():
    numbers = [1, 2, 3, 4, 5]

    # pierwszy sposob zapisu
    try:
        numbers[5]
    except IndexError as ie:
        print(f'Index Exception cached info: {ie.args}')
    except BaseException as be:
        print(f'Base Exception cached info: {be.args}')

    # drugi sposob zapisu
    try:
        numbers[5]
    except (IndexError, BaseException) as e:
        print(f'Index Exception cached info: {e.args}')

def ex2():
    pass