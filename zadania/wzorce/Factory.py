import abc
from abc import ABC
from typing import Literal


class Mage:
    def __init__(self, name: str):
        self.name = name

    def cast_spell(self, spell_name: str):
        if "basic" in spell_name.lower():
            return f"cast {spell_name}"
        return f"cast of {spell_name} failed"


class FireMage(Mage):
    def __init__(self, name: str):
        super().__init__(name)

    def cast_spell(self, spell_name: str):
        result = super().cast_spell(spell_name)
        if "fire" in spell_name:
            result = f"cast {spell_name}"
        return result


class Academy(ABC):
    @abc.abstractmethod
    def educate_mage(self, name: str):
        pass


class BasicAcademy(Academy):
    def educate_mage(self, name: str):
        return Mage(name)


class FireAcademy(Academy):
    def educate_mage(self, name: str):
        return FireMage(name)


def educate_mage(name: str, mage_type: Literal["fire", "basic"] = None):
    if mage_type == "fire":
        return FireMage(name)
    elif mage_type == "basic":
        return Mage(name)
    else:
        return None


if __name__ == "__main__":
    mag = educate_mage("Robin", "fire")
    print(mag.cast_spell("Basic fire ball"))
    print(mag.cast_spell("fire ball"))
    print(mag.cast_spell("energy Ball"))
