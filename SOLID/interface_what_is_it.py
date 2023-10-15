import abc
from typing import List

#interfejs definuje metody ktore powinny zostac zaimplementowane w klasach pochodnych
class IAnimal(abc.ABC):
    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_age(self):
        pass

    @abc.abstractmethod
    def give_sound(self):
        pass

    #tej metody nie musimy implementowac w kalsach pochodnych
    def koduj(self):
        print("kodze")

# musimy zaimplementowac metody abstakcyjne z interfejsu IAnimal
class Animal(IAnimal):
    def give_sound(self):
        print("Ani ani animal")

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal {self.name},{self.age}"


# musimy zaimplementowac metody abstakcyjne z interfejsu IAnimal
class Programista(IAnimal):
    def give_sound(self):
        print("Python Python Kod")

    def get_age(self):
        return "over 9000"

    def get_name(self):
        return "programek"


zwierzak = Animal("dog", 10)

#Funkcja wie ze dostanie obiekty typu IAnimal nie ma pojecia o Animal ani Programistach
def sound_of_animals(animals: List[IAnimal]):
    for animal in animals:
        animal.give_sound()
        animal.koduj()


sound_of_animals([zwierzak,Animal("cat",50),Programista(),Programista()])
