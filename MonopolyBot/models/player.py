import random


class Player:
    money = None
    name = None
    position = None

    def __init__(self, name: str, money: int, number_of_houses: int, number_of_hotels: int, get_out_of_jail_free_cards: int):
        self.name = name
        self.money = money
        self.position = 0
        self.number_of_houses = number_of_houses
        self.number_of_hotels = number_of_hotels
        self.get_out_of_jail_free_cards = get_out_of_jail_free_cards

    def rolling(self):
        dice_value = 2
            # random.randint(2, 12)
        self.position += dice_value
        return dice_value


