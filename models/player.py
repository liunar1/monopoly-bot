import random
from models.properties import Home, Railroad

class Player:
    money = None
    name = None
    position = None

    def __init__(self, name: str, character, money: int, number_of_houses: int, number_of_hotels: int, get_out_of_jail_free_cards: int):
        self.name = name
        self.character = character
        self.money = money
        self.position = 0
        self.number_of_houses = number_of_houses
        self.number_of_hotels = number_of_hotels
        self.in_jail = False
        self.get_out_of_jail_free_cards = get_out_of_jail_free_cards
        self.roll = True # we don't want a player to be able to randomly roll again
        self.pass_go = False
        self.new_space = False
        self.homes = {
            "brown" : [[], 2],
            "light blue" : [[], 3],
            "pink" : [[], 3],
            "orange" : [[], 3],
            "red" : [[], 3],
            "yellow" : [[], 3],
            "green" : [[], 3],
            "dark blue" : [[], 2]
        }
        self.railroads = 0 # number of railroads owned
        self.utilities = 0 # number of utilities owned
        self.adv_to_rail = False
        self.roll_for_util = False
        self.double_roll_ct = 0 # number of times player has rolled a double in a row

    def rolling(self, player):
        dice_value1 = 0
        dice_value2 = 0
        if dice_value1 == dice_value2:
            player.double_roll_ct += 1
        else:
            player.double_roll_ct = 0
        dice_value = 10
        # dice_value = random.randint(2, 12)
        player.position += dice_value
        if player.position > 40:
            player.pass_go = True
        player.position %= 40
        return dice_value
    
    def buy(self, player, property):
        property.owner = player
        player.money -= property.cost
        if type(property) == Home:
            player.homes[property.color][0].append(property)
        elif type(property) == Railroad:
            player.railroads += 1
        else:
            player.utilities += 1

    def buy_house(self, player, property):
        property.houses += 1
        player.money -= property.cost

    def buy_hotel(self, player, property): 
        # this should make the total number of houses on the property to equal 5
        property.houses += 1
        player.money -= property.cost


