class Piersi:
    def karm_dziecko(self):
        print("dziecko jest karmione.")

class SilikonowePiersi(Piersi):
    def karm_dziecko(self):
        print("dziecko jest karmione silikonowymi piersiami.")


class MamaTomka:
    def __init__(self):
        self.piersi:Piersi = SilikonowePiersi()

    def nakarm_tomka(self):
        self.piersi.karm_dziecko()

mama = MamaTomka()

mama.nakarm_tomka()