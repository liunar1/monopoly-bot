from properties import *
from space import *


class Board:

    def __init__(self, players):
        # self.bank = Player('Bank', 0)
        self.players = [],
        self.spaces = [
            # GO
            Home("Mediterranean Avenue", 60, self.bank, Color.BROWN),
            # Community Chest
            Home("Baltic Avenue", 60, self.bank, Color.BROWN),
            # Income Tax
            Railroad("Reading Railroad", 200, self.bank),
            Home("Oriental Avenue", 100, self.bank, Color.LIGHT_BLUE),
            # Chance
            Home("Vermont", 100, self.bank, Color.LIGHT_BLUE),
            Home("Connecticut", 120, self.bank, Color.LIGHT_BLUE),
            # Jail
            Home("St. Charles Place", 140, self.bank, Color.PINK),
            Utility("Electric Company", 150, self.bank),
            Home("States Avenue", 140, self.bank, Color.PINK),
            Home("Virginia Avenue", 160, self.bank, Color.PINK),
            Railroad("Pennsylvania Avenue", 200, self.bank),
            Home("St. James Place", 180, self.bank, Color.ORANGE),
            # Community Chest
            Home("Tennessee Avenue", 180, self.bank, Color.ORANGE),
            Home("New York Avenue", 200, self.bank, Color.ORANGE),
            # Free Parking
            Home("Kentucky Avenue", 220, self.bank, Color.RED),
            # Chance
            Home("Indiana Avenue", 220, self.bank, Color.RED),
            Home("Illinois Avenue", 240, self.bank, Color.RED),
            Railroad("B. & O. Railroad", 200, self.bank),
            Home("Atlantic Avenue", 260, self.bank, Color.YELLOW),
            Home("Ventnor Avenue", 260, self.bank, Color.YELLOW),
            Utility("Water Works", 150, self.bank),
            Home("Marvin Gardens", 280, self.bank, Color.YELLOW),
            # Go to Jail
            Home("Pacific Avenue", 300, self.bank, Color.GREEN),
            Home("North Carolina Avenue", 300, self.bank, Color.GREEN),
            # Community Chest
            Home("Pennsylvania Avenue", 320, self.bank, GREEN),
            Railroad("Short Line", 200, self.bank),
            # Chance
            Home("Park Place", 350, self.bank, DARK_BLUE),
            # Luxury Tax
            Home("Boardwalk", 400, self.bank, DARK_BLUE),
            ]



        ]
