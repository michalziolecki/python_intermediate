from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from queue import Queue
from random import randint
from threading import Thread, Lock, Event
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


"""
Zad 4
 Tutaj uzylem globalnie dostepnych zmiennych
 ale lepiej bylo by podziedziczyc po watku
  i przekazac referencje do tych obiektow
  tylko nie chce utrudniac wchodzac mocniej pojeciem referencji :))
"""
name = ''
data_lock = Lock()  # zabezpiecza przed jednoczesnym dostepem do zmiennych
finish_event = Event()


def write_name_loop():
    global finish_event
    global data_lock
    global name
    while True:
        try:
            in_value = input('Write name: \n')
            if in_value == 'exit':
                finish_event.set()
                break
            with data_lock:
                name = in_value
                print(f'Thread [write_name_loop] =>'
                      f' Write new name is: {name}')
        except KeyboardInterrupt:
            finish_event.set()
            break


def check_name_loop():
    global finish_event
    global data_lock
    global name
    old_name = ''
    while True:
        if finish_event.is_set():
            break
        data_lock.acquire()
        try:
            # print(f'checking name, new: {name}, old: {old_name}')
            if old_name != name:
                print(f'Thread [check_name_loop] => old name'
                      f' {old_name}, new name: {name}')
                old_name = name
        finally:
            data_lock.release()
        sleep(1)


def threading_ex4():
    writing_thread = Thread(target=write_name_loop)
    reading_thread = Thread(target=check_name_loop)
    writing_thread.start()
    reading_thread.start()
    writing_thread.join()
    reading_thread.join()


"""
Zad 5 *
Zadanie z gwiazdką bo podziedziczymy po Thread i przekażemy referencję do kolejki
"""


class Numbers:
    def __init__(self, numbers=None):
        self.numbers_list = numbers or []


class AThread(Thread):

    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            value_first = randint(0, 1000)
            value_second = randint(0, 1000)
            print(f'Random number are x={value_first} and y={value_second}')
            self.queue.put(Numbers(numbers=[value_first, value_second]))
            sleep(2)


class BThread(Thread):

    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            numbers = self.queue.get()
            if numbers:
                print(f'numbers.numbers_list'
                      f' sum = {numbers.numbers_list[0] + numbers.numbers_list [1]}')
            sleep(2)


def threading_ex5():
    queue = Queue()
    thread_a = AThread(queue)
    thread_b = BThread(queue)
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
