import enum
from typing import Optional
from models.space import Space


class Property(Space):
    def __init__(self, name: str, action, cost: int, owner):
        super().__init__(name, action)
        self.cost = cost
        self.owner = owner


class Railroad(Property):
    def __init__(self, name, action, cost, rent, owner):
        super().__init__(name, action, cost, owner)
        self.rent = rent # rent starts at 25 but multiplies based on how many railroads a player owns


class Utility(Property):
    def __init__(self, name, action, cost, rent, owner):
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
    def __init__(self, name, action, cost, rent, owner, color: Color, houses: int):
        super().__init__(name, action, cost, owner)
        self.rent = rent # array of 6 [base rent, rent1house, rent2house ... rent5house]
        self.color = color
        self.houses = houses # we will consider a hotel to equal five houses
 
