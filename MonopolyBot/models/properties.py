import enum
from typing import Optional
from models.player import Player
from models.space import Space


class Property(Space):
    def __init__(self, name: str, cost: int, owner: Optional[Player]):
        super().__init__(name)
        self.cost = cost
        self.owner = owner


class Railroad(Property):
    def __init__(self, name, cost, rent, owner: Optional[Player]):
        super().__init__(name, cost, owner)
        self.rent = rent


class Utility(Property):
    def __init__(self, name, cost, rent, owner: Optional[Player]):
        super().__init__(name, cost, owner)
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
    def __init__(self, name, cost, rent, owner: Optional[Player], color: Color, houses: int):
        super().__init__(name, cost, owner)
        self.rent = rent
        self.color = color
        self.houses = houses
