from player import *
from properties import *
from board import *
import main


class Space:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    @staticmethod
    def tax_player(self, tax: int):
        Player.money -= tax

    @staticmethod
    def property(self):
        if Property.owner == bank:
            await ctx.send('This property is unowned.')
            await ctx.send('Would you like to buy this property?')

