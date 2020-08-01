import pickle


def pickling_write():
    strings = ['a', 'b', 'c']

    try:
        with open('./data.pickle', 'wb') as fd:  # './' stands for current directory # 'b' stands for binary
            print(pickle.dumps(strings))
            pickle.dump(strings, fd)
    except (IOError, BaseException) as e:
        print(f'Problem with writing to file, info : {e.args}')


def pickling_read():
    strings = []

    try:
        with open('./data.pickle', 'rb') as fd:  # './' stands for current directory # 'b' stands for binary
            strings = pickle.load(fd)
    except (IOError, BaseException) as e:
        print(f'Problem with writing to file, info : {e.args}')

    print(strings)
