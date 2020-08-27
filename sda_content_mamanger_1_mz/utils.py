from contextlib import contextmanager


@contextmanager
def open_file(path: str):
    print('opening file')
    fd = open(path, 'a')
    yield fd
    fd.close()
    print('closing file')


def write_file(path='test.txt', text='aaa'):
    try:
        with open_file(path) as fd:
            fd.write(text)
    except IOError as e:
        print(f'IOError caught {e.args}')


class OpenFileManager:

    def __init__(self, path=""):
        self.__source = path

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, path: str):
        self.__source = path

    def __enter__(self):
        print('opening file')
        self.__file_descriptor = open(self.source, 'a')
        return self.__file_descriptor

    def __exit__(self, *args):
        print('closing file')
        self.__file_descriptor.close()


def write_file_with_object(path='test_with_obj.txt', text='aaa'):
    try:
        with OpenFileManager(path) as fd:
            fd.write(text)
    except IOError as e:
        print(f'IOError caught {e.args}')
