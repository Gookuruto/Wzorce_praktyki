import abc
from abc import ABC


class WorkBoard:
    def __init__(self):
        self.observers = set()
        self.work_offers = []

    def add_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.discard(observer)

    def add_offer(self, work_offer):
        self.work_offers.append(work_offer)
        self._notify()

    def remove_offer(self, work_offer):
        self.work_offers.remove(work_offer)
        self._notify()

    def _notify(self):
        for observer in self.observers:
            observer.update(self.work_offers)


class Observer(ABC):
    @abc.abstractmethod
    def update(self, arg):
        pass


class JobLess(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, arg):
        print("Oferty pracy:")
        print(arg)


if __name__ == "__main__":
    workboard = WorkBoard()
    human = JobLess("Bogdan")

    workboard.add_offer("spawacz 100zl/h")
    workboard.add_observer(human)
    workboard.add_offer("pogramista 15k/miesiecznie")
    workboard.remove_observer(human)
    workboard.add_offer("pogramista 15k/miesiecznie")


