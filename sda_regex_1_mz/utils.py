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
    print('Write serial id')
    value = input()
    expression = '[A-Z]{3}[0-9]{5}[a-z]{1}[A-Z]{1}'
    if re.match(expression, value):
        print('correct serial id')
    else:
        print('incorrect serial id')


def regex_ex7():
    print('Write serial')
    value = input()
    expression = '([A-Z0-9!@#\\$%\\^&\\*]{5}\\-){4}[A-Z0-9!@#\\$%\\^&\\*]{5}'
    if re.match(expression, value):
        print('correct serial')
    else:
        print('incorrect serial')


def regex_ex8():
    print('Write FV')
    value = input()
    expression = 'FV/[0-9]+/[0-9]{2}/[0-9]{4}'
    if re.match(expression, value):
        print('correct FV')
    else:
        print('incorrect FV')


def regex_ex9():
    text = """ Drogi Marszałku, Wysoka Izbo. PKB rośnie. Z pełną odpowiedzialnością mogę
    stwierdzić iż realizacja określonych zadań stanowionych przez organizację.
    Dalszy rozwój jest ważne zadanie w większym stopniu tworzenie odpowiednich
    warunków aktywizacji. Często niezauważanym szczegółem jest to, że zakres
    i rozwijanie struktur pociąga za najważniejszy punkt naszych działań
    obierzemy praktykę, nie zaś teorię, okazuje się jasne
    """
    regex = ' '
    result = re.split(regex, text)
    print(result)
    filtered_result = [element for element in result if element]
    print(filtered_result)
    print(f'Ilość słów: {len(filtered_result)}')
    print(f'Ilosc znakow: {len(text)}')
    sum_of_chars = 0
    longest_word_size = 0
    shortest_word_size = 0
    if filtered_result:
        shortest_word_size = len(filtered_result[0])
    for word in filtered_result:
        length_word = len(word)
        if length_word > longest_word_size:
            longest_word_size = length_word
        if shortest_word_size > length_word:
            shortest_word_size = length_word
        sum_of_chars += length_word
    print(f'Srednia dlugosc slowa: {float(sum_of_chars/len(filtered_result))}')
    print(f'Najdluzsze slowo: {longest_word_size}')
    print(f'Najkrotsze slowo: {shortest_word_size}')
