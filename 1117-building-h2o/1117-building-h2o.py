
from threading import Semaphore

class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(0)
        self.lock = Semaphore(1)
        self.count = 0

    def hydrogen(self, releaseHydrogen):
        self.h.acquire()

        releaseHydrogen()

        self.lock.acquire()
        self.count += 1

        if self.count == 2:
            self.o.release()

        self.lock.release()

    def oxygen(self, releaseOxygen):
        self.o.acquire()

        releaseOxygen()

        self.lock.acquire()
        self.count = 0
        self.h.release()
        self.h.release()
        self.lock.release()