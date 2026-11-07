import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Semaphore(0)
        self.second_done = threading.Semaphore(0)

    def first(self, printFirst):
        printFirst()
        self.first_done.release()

    def second(self, printSecond):
        self.first_done.acquire()
        printSecond()
        self.second_done.release()

    def third(self, printThird):
        self.second_done.acquire()
        printThird()