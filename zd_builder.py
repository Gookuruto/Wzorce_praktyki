"""
Stworz symulacje robienia kawy przy uzyciu wzorca Builder Directorem Bedzie Barista a kawa bedzie wyglada w ponizszy sposob.
zstworz builderow dla roznych kaw americana, latte, czarna itp.
"""


class Coffee:
    def __init__(self):
        seed = None
        water = None
        milk = None
        additional_ingredients = []


class Barista:
    def __init__(self):
        """Get a builder Here"""
        self.manual = None

    def set_manual(self, manual):
        self.manual = manual

    def create_coffee(self):
        pass
