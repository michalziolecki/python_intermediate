from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from random import randint
from threading import Thread
from time import sleep


class MyThread(Thread):
    def run(self):
        for i in range(1, 6, 1):
            print(f'class thread -> {i} number = {randint(10, 100)}\n')
            sleep(1)


def threading_ex1():
    my_thread = MyThread()
    my_thread.start()


def my_thread_func(how_many_numbers=5):
    for i in range(1, how_many_numbers + 1, 1):
        print(f'function in thread -> {i} number = {randint(10, 100)}\n')
        sleep(1)


def threading_ex2():
    my_thread = Thread(target=my_thread_func, args=(5,))
    my_thread.start()


def my_thread_sleeping(thread_number: int):
    while True:
        sleep(randint(1, 10))
        print(f'[thread_number={thread_number}]: date_now="{datetime.now()}"\n')


def threading_ex3():
    with ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(5):
            executor.submit(my_thread_sleeping, index)


