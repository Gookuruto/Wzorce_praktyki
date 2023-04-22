from abc import ABC, abstractmethod
from typing import Any


class Director:
    __builder = None

    def set_builder(self, builder: Any):
        self.__builder = builder

    def get_car(self):
        car = Car()
        car.set_engine(self.__builder.build_engine())
        car.set_body(self.__builder.build_body())
        for i in range(4):
            car.attach_wheel(self.__builder.build_wheel())
        return car


class DirectorThreeWheels:
    __builder = None

    def set_builder(self, builder: Any):
        self.__builder = builder

    def get_car(self):
        car = Car()
        car.set_engine(self.__builder.build_engine())
        car.set_body(self.__builder.build_body())
        for i in range(3):
            car.attach_wheel(self.__builder.build_wheel())
        return car

class Car:
    def __init__(self):
        self.__wheels = []
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print(f"body: {self.__body.shape}")
        print(f"engine horse power: {self.__engine.horsepower}")
        print(f"number of wheels: {len(self.__wheels)} ")
        print(f"tire size {self.__wheels[0].size}")


class Builder(ABC):
    @abstractmethod
    def build_wheel(self):
        pass

    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class JeepBuilder(Builder):

    def build_body(self):
        body = Body()
        body.shape = "SUV"
        return body

    def build_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def build_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_result(self):
        car = Car()
        car.set_body(self.build_body())
        car.set_engine(self.build_engine())
        for i in range(4):
            car.attach_wheel(self.build_wheel())

        return car


class SubaruBuilder(Builder):
    def build_body(self):
        body = Body()
        body.shape = "SEDAN"
        return body

    def build_engine(self):
        engine = Engine()
        engine.horsepower = 600
        return engine

    def build_wheel(self):
        wheel = Wheel()
        wheel.size = 19
        return wheel

    def get_result(self):
        car = Car()
        car.set_body(self.build_body())
        car.set_engine(self.build_engine())
        for i in range(4):
            car.attach_wheel(self.build_wheel())

        return car


class Wheel:
    size = None  # int


class Engine:
    horsepower = None  # int


class Body:
    shape = None  # str np. SUV, SEDAN, HATCHBACK


if __name__ == "__main__":
    builder = SubaruBuilder()
    director = DirectorThreeWheels()

    director.set_builder(builder)
    subaru: Car = director.get_car()
    subaru.specification()
