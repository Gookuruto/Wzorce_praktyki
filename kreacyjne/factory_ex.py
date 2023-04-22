from abc import ABC, abstractmethod


class Game(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


class GameFactory(ABC):
    @abstractmethod
    def create(self):
        pass


class BoardGame(Game):
    pass

class PCGame(Game):
    pass

class MonopolyFactory(GameFactory):
    pass

class ValorantFactory(GameFactory):
    pass



factory = MonopolyFactory()

monopoly_game = factory.create()

print(type(monopoly_game))
print(monopoly_game.get_name())