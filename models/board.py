from models.properties import *
from models.space import *
import action


class Board:
     def __init__(self, num_players: int):
          self.num_players = num_players
          self.characters = ['airplane', 'boat', 'car', 'dog', 'hat', 'magnet', 'can', 'shoe']
          self.current_player = 0
          self.players = []
          self.spaces = [
          # Home arguments: (name, action when you land on property, cost to buy, 
          # base rent, group rent, rent 1 house, rent 2 house, rent 3 house, rent 4 house, rent hotel, 
          # owner, color, num houses, num hotels)
          Space("GO", action.collect_from_go),
          Home("Mediterranean Avenue", action.land_on_property, 60, [2, 10, 30, 90, 160, 250], None, Color.BROWN, 0),
          Space("Community Chest", action.community_chest),
          Home("Baltic Avenue", action.land_on_property, 60, [4, 20, 60, 180, 320, 450], None, Color.BROWN, 0),
          Space("Income Tax", action.income_tax),
          Railroad("Reading Railroad", action.land_on_property, 200, 25, None),
          Home("Oriental Avenue", action.land_on_property, 100, [6, 30, 90, 270, 400, 550], None, Color.LIGHT_BLUE, 0),
          Space("Chance", action.chance),
          Home("Vermont", action.land_on_property, 100, [6, 30, 90, 270, 400, 550], None, Color.LIGHT_BLUE, 0),
          Home("Connecticut", action.land_on_property, 120, [8, 40, 100, 300, 450, 600], None, Color.LIGHT_BLUE, 0),
          Space("Jail", action.prison),
          Home("St. Charles Place", action.land_on_property, 140, [10, 50, 150, 450, 625, 750], None, Color.PINK, 0),
          Utility("Electric Company", action.land_on_property, 150, None, None),
          Home("States Avenue", action.land_on_property, 140, [10, 50, 150, 450, 625, 750], None, Color.PINK, 0),
          Home("Virginia Avenue", action.land_on_property, 160, [12, 60, 180, 500, 700, 900], None, Color.PINK, 0),
          Railroad("Pennsylvania Railroad", action.land_on_property, 200, 25, None),
          Home("St. James Place", action.land_on_property, 180, [14, 70, 200, 550, 750, 950], None, Color.ORANGE, 0),
          Space("Community Chest", action.community_chest),
          Home("Tennessee Avenue", action.land_on_property, 180, [14, 70, 200, 550, 750, 950], None, Color.ORANGE, 0),
          Home("New York Avenue", action.land_on_property, 200, [16, 80, 220, 600, 800, 1000], None, Color.ORANGE, 0),
          Space("Free Parking", action.free_parking),
          Home("Kentucky Avenue", action.land_on_property, 220, [18, 90, 250, 700, 875, 1050], None, Color.RED, 0),
          Space("Chance", action.chance),
          Home("Indiana Avenue", action.land_on_property, 220, [18, 90, 250, 700, 875, 1050], None, Color.RED, 0),
          Home("Illinois Avenue", action.land_on_property, 240, [20, 100, 300, 750, 925, 1100], None, Color.RED, 0),
          Railroad("B. & O. Railroad", action.land_on_property, 200, 25, None),
          Home("Atlantic Avenue", action.land_on_property, 260, [22, 110, 330, 800, 975, 1150], None, Color.YELLOW, 0),
          Home("Ventnor Avenue", action.land_on_property, 260, [22, 110, 330, 800, 975, 1150], None, Color.YELLOW, 0),
          Utility("Water Works", action.land_on_property, 150, None, None),
          Home("Marvin Gardens", action.land_on_property, 280, [24, 120, 360, 850, 1025, 1200], None, Color.GREEN, 0),
          Space("Go to Jail", action.jailed),
          Home("Pacific Avenue", action.land_on_property, 300, [26, 130, 390, 900, 1100, 1275], None, Color.GREEN, 0),
          Home("North Carolina Avenue", action.land_on_property, 300, [26, 130, 390, 900, 1100, 1275], None, Color.GREEN, 0),
          Space("Community Chest", action.community_chest),
          Home("Pennsylvania Avenue", action.land_on_property, 320, [28, 150, 450, 1000, 1200, 1400], None, Color.GREEN, 0),
          Railroad("Short Line", action.land_on_property, 200, 25, None),
          Space("Chance", action.chance),
          Home("Park Place", action.land_on_property, 350, [35, 175, 500, 1100, 1300, 1500], None, Color.DARK_BLUE, 0),
          Space("Luxury Tax", action.luxury_tax),
          Home("Boardwalk", action.land_on_property, 400, [50, 200, 600, 1400, 1700, 2000], None, Color.DARK_BLUE, 0),
          ]


games = None
