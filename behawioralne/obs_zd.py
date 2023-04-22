import abc
from abc import ABC
from typing import Set


class Celebrity:
    def __init__(self):
        self._observers: Set[Observer] = set()
        self._subject_data = None

    def add_observer(self, observer):
        self._observers.add(observer)

    def remove_observer(self, observer):
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_data)

    @property
    def subject_data(self):
        return self._subject_data

    @subject_data.setter
    def subject_data(self, data):
        self._subject_data = data
        self._notify()


class Observer(ABC):
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class Fan(Observer):
    def update(self, arg):
        if self._observer_state is None:
            self._observer_state = []
        print("Updating state from observable object")
        print(f"before: {self._observer_state}")
        self._observer_state.append(arg)
        print(f"after: {self._observer_state}")



if __name__ == "__main__":
    subject = Celebrity()
    concrete_observer = Fan()
    subject.add_observer(concrete_observer)
    subject.subject_data = "Gwiazda sie żeni."
    subject.subject_data = "Gwiazda bierze rozwod."
