import enum
from typing import Optional
from player import Player
from space import Space


class Property(Space):
    def __init__(self, name: str, action, cost: int, owner: Player):
        super().__init__(name, action)
        self.cost = cost
        self.owner = owner


class Railroad(Property):
    def __init__(self, name, action, cost, rent, owner: Player):
        super().__init__(name, action, cost, owner)
        self.rent = rent


class Utility(Property):
    def __init__(self, name, action, cost, rent, owner: Player):
        super().__init__(name, action, cost, owner)
        self.rent = rent


class Color(enum.Enum):
    BROWN = "brown"
    LIGHT_BLUE = "light blue"
    PINK = "pink"
    ORANGE = "orange"
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    DARK_BLUE = "dark blue"


class Home(Property):
    def __init__(self, name, action, cost, rent, owner: Player, color: Color, houses: int):
        super().__init__(name, action, cost, owner)
        self.rent = rent
        self.color = color
        self.houses = houses
