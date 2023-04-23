import random
import traceback


class Car:
    def __init__(self):
        self.generator = random.Random()

    def accelerate(self):
        random_num = self.generator.randint(50, 100)
        speed = random_num
        print(f"The speed of the car is {speed} mph")

    def apply_brakes(self):
        random_num = self.generator.randint(20, 40)
        speed = random_num
        print(f"The speed of the car is {speed} mph after applying the brakes")

    def assign_driver(self, driver_name):
        print(f"{driver_name} is driving the car")


class Motorcycle:
    def __init__(self):
        self.generator = random.Random()
        self.rider = None
        self.speed = 0

    def rev_throttle(self):
        random_num = self.generator.randint(50, 100)
        speed = random_num
        self.speed = speed
        print(f"The speed of the motorcycle is {speed} mph")

    def pull_brake_lever(self):
        random_num = self.generator.randint(20, 40)
        speed = random_num
        self.speed = self.speed + speed
        print(
            f"The speed of the motorcycle is {self.speed} mph after applying the brakes"
        )

    def assign_rider(self, rider_name):
        self.rider = rider_name
        print(f"{rider_name} is riding the motorcycle")


class MotorcycleAdapter:
    def __init__(self, bike: Motorcycle):
        self.bike = bike

    def accelerate(self):
        self.bike.rev_throttle()

    def apply_brakes(self):
        self.bike.pull_brake_lever()

    def assign_driver(self, driver_name):
        self.bike.assign_rider(driver_name)


if __name__ == "__main__":
    car = Car()
    bike = Motorcycle()
    adapted_bike = MotorcycleAdapter(bike)

    # print("The Motorcycle\n")
    # bike.assign_rider("Subodh")
    # bike.rev_throttle()
    # bike.pull_brake_lever()
    # print("\n")

    print("The Car\n")
    car.assign_driver("Sushant")
    car.accelerate()
    car.apply_brakes()
    print("\n")

    print("Attempting to call client methods with the service object\n")
    print(bike.rider, bike.speed)
    try:
        adapted_bike.assign_driver("Robert")
        adapted_bike.accelerate()
        adapted_bike.apply_brakes()
    except AttributeError:
        print("Oops! bike object cannot access car methods")
        traceback.print_exc()

    print(bike.rider, bike.speed)
