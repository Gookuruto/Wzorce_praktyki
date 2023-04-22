from abc import ABC, abstractmethod


class AbstractCar(ABC):

    @abstractmethod
    def get_body_type(self):
        pass


class SedanCar(AbstractCar):

    def __init__(self):
        self.body = "Sedan"

    def get_body_type(self):
        return f"Body Type: {self.body}"


class HatchbackCar(AbstractCar):

    def __init__(self):
        self.body = "Hatchback"

    def get_body_type(self):
        return f"Body Type: {self.body}"


class PickupCar(AbstractCar):

    def __init__(self):
        self.body = "Pick-up"

    def get_body_type(self):
        return f"Body Type: {self.body}"


class CarFactory():

    def build_car(self, plan):
        try:
            if plan == "Sedan":
                return SedanCar()
            elif plan == "Hatchback":
                return HatchbackCar()
            elif plan == "Pick-Up":
                return PickupCar()
            raise AssertionError("Car type is not valid.")
        except AssertionError as e:
            print(e)


class SedanFactory(CarFactory):
    def build_car(self, plan):
        return SedanCar()


class HatchbackCarFactory(CarFactory):
    def build_car(self, plan):
        return HatchbackCar()


class PickupFactory(CarFactory):
    def build_car(self, plan):
        return PickupCar()

if __name__ == "__main__":
    factory = CarFactory()

    print(factory.build_car("Sedan").get_body_type())
    print(factory.build_car("Hatchback").get_body_type())
