"""Modol."""
import abc
from abc import ABC
from typing import Set


class Observer(ABC):
    """Abstrakcyjna klasa.

    Która definiuje interfejs dla obiektów obserwatorów.
    """

    def __init__(self):
        """Inicjuje nowy obiekt Observer."""
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        """Aktualizuje stan obserwatora na podstawie stanu podmiotu."""
        pass


class Celebrity:
    """Klasa podmiotu (subject).

    Która umożliwia obserwatorom subskrybowanie zmian jej stanu.
    """

    def __init__(self):
        """Inicjuje nowy obiekt Celebrity."""
        self._observers: Set[Observer] = set()
        self._subject_data = None

    def add_observer(self, observer: Observer):
        """Dodaje obserwatora do zbioru obserwatorów.

        :param observer - obserwator dodawany do listy subskrybentów
        """
        self._observers.add(observer)

    def remove_observer(self, observer: Observer):
        """Usuwa obserwatora ze zbioru obserwatorów.

        :param observer - obiekt klasy observer
        """
        self._observers.discard(observer)

    def _notify(self):
        """Informuje wszystkich obserwatorów, że stan podmiotu się zmienił."""
        for observer in self._observers:
            observer.update(self._subject_data)

    @property
    def subject_data(self):
        """Zwraca aktualny stan podmiotu."""
        return self._subject_data

    @subject_data.setter
    def subject_data(self, data):
        """Ustawia stan podmiotu.

        informuje wszystkich obserwatorów o zmianie.
        """
        self._subject_data = data
        self._notify()


class Fan(Observer):
    """Konkretna implementacja klasy Observer.

    Która wyświetla zaktualizowany stan obserwatora.
    """

    def update(self, arg):
        """Aktualizuje stan obserwatora Fan."""
        if self._observer_state is None:
            self._observer_state = []
        print("Aktualizacja stanu z obiektu obserwowanego")
        print(f"przed: {self._observer_state}")
        self._observer_state.append(arg)
        print(f"po: {self._observer_state}")


if __name__ == "__main__":
    subject = Celebrity()
    concrete_observer = Fan()
    subject.add_observer(concrete_observer)
    subject.subject_data = "Gwiazda sie żeni."
    subject.subject_data = "Gwiazda bierze rozwod."
