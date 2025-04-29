"""
The Builder pattern is used to construct a complex object step by step.

"""

class House:
    def __init__(self):
        self.wall = None
        self.roof = None
        self.door = None

    def __str__(self):
        return f"Wall: {self.wall}, Roof: {self.roof}, Door: {self.door}"

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_wall(self, wall):
        self.house.wall = wall
        return self

    def build_roof(self, roof):
        self.house.roof = roof
        return self

    def build_door(self, door):
        self.house.door = door
        return self

    def get_house(self):
        return self.house

# Usage
builder = HouseBuilder()
house = builder.build_wall("Brick Wall").build_roof("Tile Roof").build_door("Wooden Door").get_house()
print(house)  # Wall: Brick Wall, Roof: Tile Roof, Door: Wooden Door
