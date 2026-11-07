
from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n

        self.fizz_sem = Semaphore(0)
        self.buzz_sem = Semaphore(0)
        self.fizzbuzz_sem = Semaphore(0)
        self.num_sem = Semaphore(1)

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                self.fizz_sem.acquire()
                printFizz()
                self.num_sem.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 5 == 0 and i % 3 != 0:
                self.buzz_sem.acquire()
                printBuzz()
                self.num_sem.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 15 == 0:
                self.fizzbuzz_sem.acquire()
                printFizzBuzz()
                self.num_sem.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.num_sem.acquire()

            if i % 15 == 0:
                self.fizzbuzz_sem.release()
            elif i % 3 == 0:
                self.fizz_sem.release()
            elif i % 5 == 0:
                self.buzz_sem.release()
            else:
                printNumber(i)
                self.num_sem.release()