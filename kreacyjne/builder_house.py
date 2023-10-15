

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self,builder):
        self.builder = builder

    def build_home_with_pool(self):
        self.builder.build_
class HouseBuilder:
    def __init__(self):
        self.current_house = None

    def build_walls(self):
        pass

    def build_doors(self):
        pass
    def build_windows(self):
        pass

    def build_roof(self):
        pass

    def build_garage(self):
        pass

    def build_swimmingpool(self):
        pass

    def get_result(self):
        return House