from models.properties import *
from models.space import *
import action


class Board:
    def __init__(self, num_players: int):
        self.num_players = num_players
        self.currentPlayer = None
        self.players = []
        self.spaces = [
            # GO
            Home("Mediterranean Avenue", action.land_on_property, 60, 2, None, Color.BROWN, 0),
            # Community Chest
            Home("Baltic Avenue", action.land_on_property, 60, 4, None, Color.BROWN, 0),
            # Income Tax
            Railroad("Reading Railroad", action.land_on_property, 200, 25, None),
            Home("Oriental Avenue", action.land_on_property, 100, 6, None, Color.LIGHT_BLUE, 0),
            # Chance
            Home("Vermont", action.land_on_property, 100, 6, None, Color.LIGHT_BLUE, 0),
            Home("Connecticut", action.land_on_property, 120, 8, None, Color.LIGHT_BLUE, 0),
            # Jail
            Home("St. Charles Place", action.land_on_property, 140, 10, None, Color.PINK, 0),
            Utility("Electric Company", action.land_on_property, 150, None, None),
            Home("States Avenue", action.land_on_property, 140, 10, None, Color.PINK, 0),
            Home("Virginia Avenue", action.land_on_property, 160, 12, None, Color.PINK, 0),
            Railroad("Pennsylvania Railroad", action.land_on_property, 200, 25, None),
            Home("St. James Place", action.land_on_property, 180, 14, None, Color.ORANGE, 0),
            # Community Chest
            Home("Tennessee Avenue", action.land_on_property, 180, 14, None, Color.ORANGE, 0),
            Home("New York Avenue", action.land_on_property, 200, 16, None, Color.ORANGE, 0),
            # Free Parking
            Home("Kentucky Avenue", action.land_on_property, 220, 18, None, Color.RED, 0),
            # Chance
            Home("Indiana Avenue", action.land_on_property, 220, 18, None, Color.RED, 0),
            Home("Illinois Avenue", action.land_on_property, 240, 20, None, Color.RED, 0),
            Railroad("B. & O. Railroad", action.land_on_property, 200, 25, None),
            Home("Atlantic Avenue", action.land_on_property, 260, 22, None, Color.YELLOW, 0),
            Home("Ventnor Avenue", action.land_on_property, 260, 22, None, Color.YELLOW, 0),
            Utility("Water Works", action.land_on_property, 150, None, None),
            Home("Marvin Gardens", action.land_on_property, 280, 24, None, Color.GREEN, 0),
            # Go to Jail
            Home("Pacific Avenue", action.land_on_property, 300, 26, None, Color.GREEN, 0),
            Home("North Carolina Avenue", action.land_on_property, 300, 26, None, Color.GREEN, 0),
            # Community Chest
            Home("Pennsylvania Avenue", action.land_on_property, 320, 28, None, Color.GREEN, 0),
            Railroad("Short Line", action.land_on_property, 200, 25, None),
            # Chance
            Home("Park Place", action.land_on_property, 350, 35, None, Color.DARK_BLUE, 0),
            # Luxury Tax
            Home("Boardwalk", action.land_on_property, 400, 50, None, Color.DARK_BLUE, 0),
        ]


board = None
