import decimal


class Pizza:
    def __init__(self):
        self.base_price: decimal = 20.0

    def get_price(self) -> decimal:
        return self.base_price

    def __str__(self):
        return f"Pizza: {self.get_price()}"


class Mozzarella(Pizza):
    def __init__(self, base_pizza: Pizza, ilosc: int = 1):
        super().__init__()
        self.mozerella_price = 12
        self.base_pizza = base_pizza

    def get_price(self) -> decimal:
        return self.base_pizza.get_price() + self.mozerella_price


class Pepperoni(Pizza):
    def __init__(self, base_pizza: Pizza):
        super().__init__()
        self.pepperoni_price = 3
        self.base_pizza = base_pizza

    def get_price(self) -> decimal:
        return self.base_pizza.get_price() + self.pepperoni_price


pizza = Pizza()
print(pizza)

mozzarella = Mozzarella(pizza)
print(mozzarella)

pepperoni = Mozzarella(pizza)
for i in range(3):
    pepperoni = Pepperoni(pepperoni)
print(pepperoni)
