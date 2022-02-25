from models.properties import *
from models.space import *


class Board:
    def __init__(self, num_players: int):
        self.num_players = num_players
        self.players = []
        self.spaces = [
            # GO
            Home("Mediterranean Avenue", 60, 2, None, Color.BROWN, 0),
            # Community Chest
            Home("Baltic Avenue", 60, 4, None, Color.BROWN, 0),
            # Income Tax
            Railroad("Reading Railroad", 200, 25, None),
            Home("Oriental Avenue", 100, 6, None, Color.LIGHT_BLUE, 0),
            # Chance
            Home("Vermont", 100, 6, None, Color.LIGHT_BLUE, 0),
            Home("Connecticut", 120, 8, None, Color.LIGHT_BLUE, 0),
            # Jail
            Home("St. Charles Place", 140, 10, None, Color.PINK, 0),
            Utility("Electric Company", 150, None, None),
            Home("States Avenue", 140, 10, None, Color.PINK, 0),
            Home("Virginia Avenue", 160, 12, None, Color.PINK, 0),
            Railroad("Pennsylvania Avenue", 200, 25, None),
            Home("St. James Place", 180, 14, None, Color.ORANGE, 0),
            # Community Chest
            Home("Tennessee Avenue", 180, 14, None, Color.ORANGE, 0),
            Home("New York Avenue", 200, 16, None, Color.ORANGE, 0),
            # Free Parking
            Home("Kentucky Avenue", 220, 18, None, Color.RED, 0),
            # Chance
            Home("Indiana Avenue", 220, 18, None, Color.RED, 0),
            Home("Illinois Avenue", 240, 20, None, Color.RED, 0),
            Railroad("B. & O. Railroad", 200, 25, None),
            Home("Atlantic Avenue", 260, 22, None, Color.YELLOW, 0),
            Home("Ventnor Avenue", 260, 22, None, Color.YELLOW, 0),
            Utility("Water Works", 150, None, None),
            Home("Marvin Gardens", 280, 24, None, Color.GREEN, 0),
            # Go to Jail
            Home("Pacific Avenue", 300, 26, None, Color.GREEN, 0),
            Home("North Carolina Avenue", 300, 26, None, Color.GREEN, 0),
            # Community Chest
            Home("Pennsylvania Avenue", 320, 28, None, Color.GREEN, 0),
            Railroad("Short Line", 200, 25, None),
            # Chance
            Home("Park Place", 350, 35, None, Color.DARK_BLUE, 0),
            # Luxury Tax
            Home("Boardwalk", 400, 50, None, Color.DARK_BLUE, 0),
        ]


board = None
