"""
Dependency Inversion Principle
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.
"""
from abc import ABC, abstractmethod


class LightBulb:
    def turn_on(self):
        print("LightBulb: Turned on.")

    def turn_off(self):
        print("LightBulb: Turned off.")


class PowerSwitch:
    def __init__(self, l: LightBulb):
        self.l = l
        self.on = False

    def press(self):
        if self.on:
            self.l.turn_off()
            self.on = False
        else:
            self.l.turn_off()
            self.on = True


"""
Switch depend on Light bulb it's quite problematic if our switch would like to use something other.
"""


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Turned on.")

    def turn_off(self):
        print("LightBulb: Turned off.")


class Komputer(Switchable):
    def turn_on(self):
        print("Komputer: Turned on.")

    def turn_off(self):
        print("Komputer: Turned off.")


class PowerSwitch:
    def __init__(self, l: Switchable):
        self.l = l
        self.on = False

    def press(self):
        if self.on:
            self.l.turn_off()
            self.on = False
        else:
            self.l.turn_on()
            self.on = True


pc = Komputer()
l = LightBulb()

pc_Switch = PowerSwitch(pc)
light_switch = PowerSwitch(l)

pc_Switch.press()
light_switch.press()
