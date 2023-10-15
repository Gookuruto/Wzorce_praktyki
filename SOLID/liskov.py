class Piersi:
    def karm_dziecko(self):
        print("dziecko jest karmione.")


class SilikonowePiersi(Piersi):
    #Liskov jest spełniony
    def karm_dziecko(self):
        print("dziecko jest karmione silikonowymi piersiami.")

class PlastikowePiersi(Piersi):
    #Lamimy zasade podstawienia liskov bo popsujemy mame tomka
    def karm_dziecko(self):
        raise Exception("popsute")


class MamaTomka:
    def __init__(self):
        self.piersi: Piersi = PlastikowePiersi()

    def nakarm_tomka(self):
        self.piersi.karm_dziecko()


mama = MamaTomka()

mama.nakarm_tomka()
