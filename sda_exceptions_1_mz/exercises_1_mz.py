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


def ex2(name: str):
    if len(name) <= 0:
        raise ValueError('String is empty')
    print(f'value: {name}')


def ex3(number: int, divisor: int):
    result = 0
    try:
        result = number / divisor
    except ZeroDivisionError as err:
        print(f'Error cached, info: {err.args}')

    return result


def ex4(dictionary: dict):
    key = 'items'
    try:
        items = dictionary[key]
        for item in items:
            print(item)
    except KeyError as e:
        print(f'Key error info: {e.args}')


def ex4_v2(dictionary: dict):
    key = 'items'
    items = dictionary.get(key, [])
    for item in items:
        print(item)


def ex6():
    raise NotImplementedError()


def ex7():
    fd = None
    try:
        fd = open('C:\\windows-version.txt')  # fd stands for file descriptor - in system it's handler to file
        # fd.close()
    except IOError as ioe:
        print('exception while opening file info:' + str(ioe.args))
    finally:
        if fd:
            print('closing file handler if exist')
            fd.close()

    # sposób drugi
    try:
        with open('c:/not_exist/file') as fd2: # konstrukcja with pilnuje zamkniecia uchwytu do pliku pliku
            print('Plik w tym zasiegu jest otwarty')
    except IOError as ioe:
        print('exception while opening file info:' + str(ioe.args))
