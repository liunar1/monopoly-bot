from properties import *


class Board:
    def __init__(self, players):
        self.bank = Player('Bank', 0)
        self.players = [],
        self.spaces = [
            Home("Mediterranean Avenue", 60, self.bank),
            Home("Baltic Avenue", 60, self.bank),
            Railroad("Reading Railroad", 200, self.bank),
            Home("Oriental Avenue", 100, self.bank),
            Home("Vermont", 100, self.bank),
            Home("Connecticut", 120, self.bank),
            Home("St. Charles Place", 140, self.bank),
            Utility("Electric Company", 150, self.bank),
            Home("States Avenue", 140, self.bank),
            Home("Virginia Avenue", 160, self.bank),
            Railroad("Pennsylvania Avenue", 200, self.bank),
        ]
