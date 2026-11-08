
from threading import Condition
from collections import deque

class DiningPhilosophers:

    def __init__(self):
        self.cv = Condition()
        self.waiting = deque()
        self.busy = set()

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        left = philosopher
        right = (philosopher + 1) % 5
        forks = {left, right}
        request = object()

        with self.cv:
            self.waiting.append((request, forks))

            while True:
                conflict = False

                for req, other_forks in self.waiting:
                    if req is request:
                        break

                    if forks & other_forks:
                        conflict = True
                        break

                if not (forks & self.busy) and not conflict:
                    break

                self.cv.wait()

            self.waiting.remove((request, forks))
            self.busy.update(forks)

        try:
            pickLeftFork()
            pickRightFork()

            try:
                eat()
            finally:
                putLeftFork()
                putRightFork()

        finally:
            with self.cv:
                self.busy.difference_update(forks)
                self.cv.notify_all()