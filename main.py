"""Main scripts for tests."""
import abc
from abc import ABC
from typing import Any, Set


class Observer(ABC):
    @abc.abstractmethod
    def update(self, arg: Any) -> None:
        """Update method."""


class WorkBoard:
    """Workboard class."""

    def __init__(self) -> None:
        self.observers: Set[Observer] = set()
        self.work_offers = []

    def add_observer(self, observer: Observer) -> None:
        """Adding new observer.

        :param
            observer - observator for observer object
        """
        self.observers.add(observer)

    def remove_observer(self, observer: Observer) -> None:
        """Remove observer."""
        self.observers.discard(observer)

    def add_offer(self, work_offer):
        """Add offer."""
        self.work_offers.append(work_offer)
        self._notify()

    def remove_offer(self, work_offer):
        """Remove offer."""
        self.work_offers.remove(work_offer)
        self._notify()

    def _notify(self):
        for observer in self.observers:
            observer.update(self.work_offers)


class JobLess(Observer):
    def __init__(self, name: str):
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
