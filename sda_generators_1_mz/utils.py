from sda_generators_1_mz.my_iterable import MyIterable


def iterators_ex1():
    print('exercise 1')
    dictionary = {
        1: 'A',
        2: 'B',
        3: 'C'
    }

    print('keys:')
    for key in dictionary.keys():
        print(key)

    print('values:')
    for value in dictionary.values():
        print(value)


def numbers_creator(n: int) -> list:
    numb_container = []
    for i in range(n):
        numb_container.append(i)
    return numb_container


def iterators_ex2():
    print('exercise 2')
    import sys
    number_list = numbers_creator(1000)
    print(f'size of list in bytes: {sys.getsizeof(number_list)}')
    result = sum(number_list)
    print(f'size of one number in bytes: {sys.getsizeof(2)}')
    print(f'result = {result}')


def iterators_ex3():
    print('exercise 3')
    import sys
    my_iterable_obj = MyIterable(1000)
    print(f'size of list in bytes: {sys.getsizeof(my_iterable_obj)}')
    result = sum(my_iterable_obj)
    print(f'size of one number in bytes: {sys.getsizeof(2)}')
    print(f'result = {result}')


def lazy_read_in_chunks(file_descriptor, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_descriptor.read(chunk_size)
        if not data:
            break
        yield data  # zwraca dane po trochu oszczedzajac w ten sposob RAM


def generators_ex4():
    print('Exercise 4')
    with open('generators_training.txt') as f:
        for piece in lazy_read_in_chunks(f):
            print(piece)


def generators_ex5():
    """
    Domyslnie konstrukcja czytania linia po linii
     wykorzystuje generator dla oszczedzania pamieci. Przyklad konstrukcji
      for line in open()
    :return:
    """
    print('Exercise 5')
    for line in open('generators_training.txt'):
        print(line, end='')
