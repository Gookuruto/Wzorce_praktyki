import abc
import copy
from abc import ABC


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 6:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car


# The whole product
class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)
        print(f"number of wheels: {len(self.__wheels)}")


class Builder(ABC):
    @abc.abstractmethod
    def getWheel(self): pass

    @abc.abstractmethod
    def getEngine(self): pass

    @abc.abstractmethod
    def getBody(self): pass


class JeepBuilder(Builder):

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

    def get_result(self):
        car = Car()

        # First goes the body
        body = self.getBody()
        car.setBody(body)

        # Then engine
        engine = self.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 6:
            wheel = self.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car

class SubaruBuilder(Builder):

    def getBody(self):
        body = Body()
        body.shape = "Sedan"
        return body

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 600
        return engine

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel


# Car parts
class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None

def change_car(car:Car):
    eng = Engine()
    eng.horsepower = 15
    car.setEngine(eng)
    return car

def main():
    jeepBuilder = SubaruBuilder()  # initializing the class

    director = Director()

    # Build Jeep
    print("Subaru")
    director.setBuilder(jeepBuilder)
    subaru = director.getCar()
    subaru.specification()
    new_subaru = change_car(copy.copy(subaru))

    subaru.specification()
    print("______________________")
    new_subaru.specification()
    # subarus = []
    # for i in range(10):
    #     subarus.append(copy.copy(subaru))
    # for i in subarus:
    #     print("-------------------------------")
    #     i.specification()
    print("")

if __name__ == "__main__":
    main()