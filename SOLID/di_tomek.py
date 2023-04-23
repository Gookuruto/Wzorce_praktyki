import abc
from abc import ABC


class IBlondynka(ABC):
    @abc.abstractmethod
    def blond(self):
        pass


class IPiersiasta(ABC):
    @abc.abstractmethod
    def piersi(self):
        pass


class Kasia(IPiersiasta):
    def piersi(self):
        print("piersi sa macane.")


class Asia(IBlondynka):

    def blond(self):
        return "blond"


class Tomek:
    def __init__(self, ukochana: IPiersiasta):
        self.ukochana: IPiersiasta = ukochana

    def podziwiaj_blond_wlosy(self):
        if self.ukochana.blond() != "blond":
            raise Exception()
        else:
            print("Tomek podiwia włosy.")

    def macaj_piersi(self):
        self.ukochana.piersi()


kasia = Kasia()
tomek = Tomek(kasia)

tomek.macaj_piersi()


class IUmiesniony(ABC):
    @abc.abstractmethod
    def miesnie(self):
        pass


class Norbert:
    def boiler(self):
        print("macaj boiler")


class Ronaldo(IUmiesniony):
    def miesnie(self):
        print("miesnie sa macane")


class IDojzalosc(ABC):
    def posprzataj(self):
        pass

    def naprawic_zlew(self):
        pass


class Eliza:
    def __init__(self, ukochany: IUmiesniony):
        self.ukochany: IUmiesniony = ukochany

    def macaj_miesnie(self):
        self.ukochany.miesnie()

    def zmien_ukochanego(self, nowy_ukochany: IUmiesniony):
        self.ukochany = nowy_ukochany


eliza = Eliza(Ronaldo())

eliza.macaj_miesnie()

eliza.zmien_ukochanego(Ronaldo())
