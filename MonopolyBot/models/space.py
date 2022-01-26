import board
import player


class Space:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def tax(self, tax: int):
        player.Player.money -= tax
