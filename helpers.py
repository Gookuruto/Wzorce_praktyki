from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self._observers = []
        self._state = ""

    def add_observer(self, observer: "ConcreteObserver"):
        observer._subject = self
        self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
        else:
            raise ValueError(f"Observer {observer} do not exists")

    def _notify(self):
        for observer in self._observers:
            observer.update(self._state)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        self._notify()


class Observer(ABC):
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abstractmethod
    def update(self, arg):
        pass


class ConcreteObserver(Observer):

    def update(self, arg):
        self._observer_state = arg
        print(f"Subject state changed: {arg}")


if __name__ == "__main__":
    subject = Subject()
    concrete_observer = ConcreteObserver()
    subject.add_observer(concrete_observer)
    subject.state = 123