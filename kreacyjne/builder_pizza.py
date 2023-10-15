from abc import ABC, abstractmethod
from typing import Optional


class Pizza:
    def __init__(self):
        self.dought = "cienkie"
        self.sauce = "pomidorowy"
        self.cheese = "mozzarella fior di latte"
        self.ingredients = []

    def __repr__(self):
        return f"Pizza na ciescie {self.dought} z sosem {self.sauce} serem: {self.cheese} i składnikami {self.ingredients}"


class IBuilder(ABC):
    @abstractmethod
    def make_dought(self, rodzaj: str):
        pass

    @abstractmethod
    def add_cheese(self, cheese_type: str):
        pass

    @abstractmethod
    def add_sauce(self, type: str):
        pass

    @abstractmethod
    def add_ingredients(self, ingredient: str):
        pass

    @abstractmethod
    def reset(self):
        pass


class MasterChef:
    def __init__(self):
        self.underling: Optional[IBuilder] = None

    def choose_underling(self, underling: IBuilder):
        self.underling = underling

    def make(self, type: str):
        if self.underling is None:
            return None
        self.underling.reset()
        if type == "pepperoni":
            self.underling.make_dought("cienkie")
            self.underling.add_sauce("pomidorowy")
            self.underling.add_cheese("mozzarella")
            self.underling.add_ingredients("pepperoni")
            self.underling.add_ingredients("kukurydza")
        elif type == "vegetariana":
            self.underling.make_dought("cienkie")
            self.underling.add_sauce("pomidorowy")
            self.underling.add_cheese("mozzarella")
            self.underling.add_ingredients("kukurydza")
            self.underling.add_ingredients("oliwki")
            self.underling.add_ingredients("papryka")

        return self.underling.bake_pizza()


class VegeUnderling(IBuilder):


    def __init__(self):
        self.pizza = Pizza()

    def reset(self):
        self.pizza = Pizza()

    def add_ingredients(self, ingredient: str):
        if ingredient in ["tofu", "vege mieso", "kukurydza", "papryka", "oliwki"]:
            self.pizza.ingredients.append(ingredient)

    def add_sauce(self, type: str):
        self.pizza.sauce = type

    def add_cheese(self, cheese_type: str):
        self.pizza.cheese = cheese_type

    def make_dought(self, rodzaj: str):
        self.pizza.dought = rodzaj

    def bake_pizza(self):
        return self.pizza


class MeatUnderling(IBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def reset(self):
        self.pizza = Pizza()

    def add_ingredients(self, ingredient: str):
        self.pizza.ingredients.append(ingredient)

    def add_sauce(self, type: str):
        self.pizza.sauce = type

    def add_cheese(self, cheese_type: str):
        self.pizza.cheese = cheese_type

    def make_dought(self, rodzaj: str):
        self.pizza.dought = rodzaj

    def bake_pizza(self):
        return self.pizza


szef = MasterChef()
vege = VegeUnderling()
meat = MeatUnderling()

szef.choose_underling(meat)
print(szef.make("pepperoni"))

szef.choose_underling(vege)
print(szef.make("pepperoni"))
szef.choose_underling(meat)
print(szef.make("vegetariana"))

szef.choose_underling(meat)
print(szef.make("vegetariana"))
