import enum
from typing import Optional
from models.player import Player
from models.space import Space


class Property(Space):
    def __init__(self, name: str, action, cost: int, owner: Optional[Player]):
        super().__init__(name, action)
        self.cost = cost
        self.owner = owner


class Railroad(Property):
    def __init__(self, name, action, cost, rent, owner: Optional[Player]):
        super().__init__(name, action, cost, owner)
        self.rent = rent


class Utility(Property):
    def __init__(self, name, action, cost, rent, owner: Optional[Player]):
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
    def __init__(self, name, action, cost, rent, group_rent, rent_house1, rent_house2, rent_house3, rent_house4, rent_hotel, owner: Optional[Player], color: Color, houses: int, hotels: int):
        super().__init__(name, action, cost, owner)
        self.rent = rent
        self.group_rent = group_rent
        self.rent_house1 = rent_house1
        self.rent_house2 = rent_house2
        self.rent_house3 = rent_house3
        self.rent_house4 = rent_house4
        self.rent_hotel = rent_hotel
        self.color = color
        self.houses = houses
        self.hotels = hotels

