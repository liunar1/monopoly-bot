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

    '''
    def buy_property(self, ctx):
        Property.owner = Player
        await ctx.reply(f'{Player.name} now owns {Property.name}')
    
    
    def buy_house(self, ctx, number_of_houses):
        Property.houses += number_of_houses
        await ctx.reply(f'{Property.name} now has {x number (undeclared variable} number of houses')
    '''
