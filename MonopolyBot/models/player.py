import random


class Player:
    money = None
    name = None
    position = None

    def __init__(self, name: str, money: int, number_of_houses: int):
        self.name = name
        self.money = money
        self.position = 0
        self.number_of_houses = number_of_houses

    def rolling(self):
        dice_value = random.randint(2, 12)
        self.position += dice_value
        return dice_value


