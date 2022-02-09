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
'''
no clue where this is supposed to go or what this is supposed to be so I'm leaving it as a comment here; should this be
a dictionary, list... ??? wtf??? there has to be a better way to do this bro
        if Home.color == BROWN:
            if Home.houses = 1:
                rent = 5 * rent
            if Home.houses = 2:
                rent = 3 * rent (previously updated rent with one house)
            if Home.houses = 3:
                rent = 3 * rent (previously updated rent with one house)
            if Home.houses = 4:
                rent = rent(1 house) * 16
            if Home.houses = 5:
                if Home.name is "Mediterranean Avenue": 
                    rent = 250
                if Home.name is "Baltic Avenue":
                    rent = 450
        if Home.color == LIGHT_BLUE:
            if Home.houses = 1:
            if Home.houses = 2:
            if Home.houses = 3:
            if Home.houses = 4:
            if Home.houses = 5:
        if Home.color == PINK:
            if Home.houses = 1:
            if Home.houses = 2:
            if Home.houses = 3:
            if Home.houses = 4:
            if Home.houses = 5:
        if Home.color == ORANGE:
            if Home.houses = 1:
            if Home.houses = 2:
            if Home.houses = 3:
            if Home.houses = 4:
            if Home.houses = 5:
        if Home.color == RED:
            if Home.houses = 1:
            if Home.houses = 2:
            if Home.houses = 3:
            if Home.houses = 4:
            if Home.houses = 5:
        if Home.color == YELLOW:
            if Home.houses = 1:
            if Home.houses = 2:
            if Home.houses = 3:
            if Home.houses = 4:
            if Home.houses = 5:
        if Home.color == GREEN:
            if Home.houses = 1:
            if Home.houses = 2:
            if Home.houses = 3:
            if Home.houses = 4:
            if Home.houses = 5:
        if Home.color == DARK_BLUE:
            if Home.houses = 1:
            if Home.houses = 2:
            if Home.houses = 3:
            if Home.houses = 4:
            if Home.houses = 5:
'''




