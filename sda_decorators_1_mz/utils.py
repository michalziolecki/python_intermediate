from functools import wraps


def my_wrapper(func):
    def wrapper(*args, **kwargs):
        print('Before')
        result = func(*args, **kwargs)
        print('after')
        return result

    return wrapper


def my_simply_wrapper(func):
    def wrapper():
        print('Before')
        result = func()
        print('after')
        return result

    return wrapper


@my_wrapper
def hello_function():
    print('Hello')


def check_file_wrapper(func):
    def inner(*args, **kwargs):
        path = ''
        if len(args) > 0:
            path = args[0]
        elif kwargs.get('file_path', ''):
            path = kwargs.get('file_path')
        import os
        if path and os.path.exists(path):
            print('Path exists')
        else:
            print('Path not exist - file created')
            from pathlib import Path
            Path(path).touch()
        return func(*args, *kwargs)

    return inner


@check_file_wrapper
def open_file_func(file_path: str, text_lines: list):
    with open(file_path, 'r') as fd:
        for line in text_lines:
            fd.write(line)


def catch_io_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as e:
            print(f'io error caught info: {e.args}')
            return None

    return inner


@catch_io_error
def throw_exception_file():
    raise IOError('test error')


@catch_io_error
def no_exist_file():
    path = 'NOT_exist_path'
    with open(path, 'r') as fd:
        fd.read()


def io_error_wrapper_by_library(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IOError as e:
            print(f'io error caught by functools.wraps info: {e.args}')

    return wrapper


@io_error_wrapper_by_library
def ex_5_no_exist_file():
    path = 'NOT_exist_path'
    with open(path, 'r') as fd:
        fd.read()
