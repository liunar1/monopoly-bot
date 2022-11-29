import random
from models.properties import Home, Railroad
from models.board import games


class Player:
    money = None
    name = None
    position = None

    def __init__(self, name: str, character: str, money: int, number_of_houses: int, number_of_hotels: int, get_out_of_jail_free_cards: int):
        self.name = name
        self.character = character
        self.characterx = 1700
        self.charactery = 1700
        self.money = money
        self.position = 0
        self.number_of_houses = number_of_houses
        self.number_of_hotels = number_of_hotels
        self.in_jail = False
        self.get_out_of_jail_free_cards = get_out_of_jail_free_cards
        self.roll = True # we don't want a player to be able to randomly roll again
        self.pass_go = False
        self.new_space = False
        self.properties = {
            "homes" : {
                "brown" : [[], 2],
                "light blue" : [[], 3],
                "pink" : [[], 3],
                "orange" : [[], 3],
                "red" : [[], 3],
                "yellow" : [[], 3],
                "green" : [[], 3],
                "dark blue" : [[], 2]
            },  
            "railroads" : [],
            "utilities" : []
        }
        self.homes = 0
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
        dice_value = 1
        # dice_value = random.randint(2, 12)
        player.position += dice_value
        if player.position > 40:
            player.pass_go = True
        player.position %= 40
        player.characterx, player.charactery = games[0].spaces[player.position].coords
        return dice_value
    
    def buy(self, player, property, position):
        property.owner = player
        player.money -= property.cost
        if type(property) == Home:
            player.properties["homes"][property.color.value][0].append(position)
        elif type(property) == Railroad:
            player.properties["railroads"].append(position)
            player.railroads += 1
        else:
            player.properties["utilities"].append(position)
            player.utilities += 1

    def buy_house(self, player, property):
        property.houses += 1
        player.number_of_houses += 1
        player.money -= property.house_cost

    def buy_hotel(self, player, property): 
        # this should make the total number of houses on the property to equal 5
        property.houses += 1
        player.number_of_hotels += 1
        player.money -= property.house_cost
    
    def sell(self, player, property, position):
        property.owner = None
        player.money += property.cost / 2
        if type(property) == Home:
            player.properties["homes"][property.color.value][0].remove(position)
        elif type(property) == Railroad:
            player.properties["railroads"].remove(position)
            player.railroads -= 1
        else:
            player.properties["utilities"].remove(position)
            player.utilities -= 1
    
    def sell_house(self, player, property):
        property.houses -= 1
        player.number_of_houses -= 1
        player.money += property.house_cost / 2

    def sell_hotel(self, player, property): 
        # the total number of houses on the property must be equal to 5
        property.houses -= 1
        player.number_of_hotels -= 1
        player.money += property.house_cost / 2


