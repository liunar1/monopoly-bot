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
          # tuples at the end: (x1, y1) (x2, y2) where x1 and y1 represent where the piece lands and x2 and y2 represent where to 
          # indicate ownership of a property 
          Space("GO", action.collect_from_go, (1710, 1705)),
          Home("Mediterranean Avenue", action.land_on_property, 60, [2, 10, 30, 90, 160, 250], None, Color.BROWN, 0, (1495, 1705)),
          Space("Community Chest", action.community_chest, (1345, 1705)),
          Home("Baltic Avenue", action.land_on_property, 60, [4, 20, 60, 180, 320, 450], None, Color.BROWN, 0, (1195, 1705)),
          Space("Income Tax", action.income_tax, (1045, 1705)),
          Railroad("Reading Railroad", action.land_on_property, 200, 25, None, (895, 1705)),
          Home("Oriental Avenue", action.land_on_property, 100, [6, 30, 90, 270, 400, 550], None, Color.LIGHT_BLUE, 0, (745, 1705)),
          Space("Chance", action.chance, (595, 1705)),
          Home("Vermont", action.land_on_property, 100, [6, 30, 90, 270, 400, 550], None, Color.LIGHT_BLUE, 0, (445, 1705)),
          Home("Connecticut", action.land_on_property, 120, [8, 40, 100, 300, 450, 600], None, Color.LIGHT_BLUE, 0, (295, 1705)),
          Space("Jail", action.prison, (100, 1705)),
          Home("St. Charles Place", action.land_on_property, 140, [10, 50, 150, 450, 625, 750], None, Color.PINK, 0, (90, 1490)),
          Utility("Electric Company", action.land_on_property, 150, None, None, (90, 1340)),
          Home("States Avenue", action.land_on_property, 140, [10, 50, 150, 450, 625, 750], None, Color.PINK, 0, (90, 1190)),
          Home("Virginia Avenue", action.land_on_property, 160, [12, 60, 180, 500, 700, 900], None, Color.PINK, 0, (90, 1040)),
          Railroad("Pennsylvania Railroad", action.land_on_property, 200, 25, None, (90, 895)),
          Home("St. James Place", action.land_on_property, 180, [14, 70, 200, 550, 750, 950], None, Color.ORANGE, 0, (90, 745)),
          Space("Community Chest", action.community_chest, (90, 595)),
          Home("Tennessee Avenue", action.land_on_property, 180, [14, 70, 200, 550, 750, 950], None, Color.ORANGE, 0, (90, 445)),
          Home("New York Avenue", action.land_on_property, 200, [16, 80, 220, 600, 800, 1000], None, Color.ORANGE, 0, (90, 300)),
          Space("Free Parking", action.free_parking, (100, 100)),
          Home("Kentucky Avenue", action.land_on_property, 220, [18, 90, 250, 700, 875, 1050], None, Color.RED, 0, (295, 90)),
          Space("Chance", action.chance, (445, 100)),
          Home("Indiana Avenue", action.land_on_property, 220, [18, 90, 250, 700, 875, 1050], None, Color.RED, 0, (595, 90)),
          Home("Illinois Avenue", action.land_on_property, 240, [20, 100, 300, 750, 925, 1100], None, Color.RED, 0, (745, 90)),
          Railroad("B. & O. Railroad", action.land_on_property, 200, 25, None, (895, 100)),
          Home("Atlantic Avenue", action.land_on_property, 260, [22, 110, 330, 800, 975, 1150], None, Color.YELLOW, 0, (1045, 90)),
          Home("Ventnor Avenue", action.land_on_property, 260, [22, 110, 330, 800, 975, 1150], None, Color.YELLOW, 0, (1195, 90)),
          Utility("Water Works", action.land_on_property, 150, None, None, (1345, 90)),
          Home("Marvin Gardens", action.land_on_property, 280, [24, 120, 360, 850, 1025, 1200], None, Color.GREEN, 0, (1495, 90)),
          Space("Go to Jail", action.go_to_jail, (1700, 90)),
          Home("Pacific Avenue", action.land_on_property, 300, [26, 130, 390, 900, 1100, 1275], None, Color.GREEN, 0, (1710, 300)),
          Home("North Carolina Avenue", action.land_on_property, 300, [26, 130, 390, 900, 1100, 1275], None, Color.GREEN, 0, (1710, 445)),
          Space("Community Chest", action.community_chest, (1710, 595)),
          Home("Pennsylvania Avenue", action.land_on_property, 320, [28, 150, 450, 1000, 1200, 1400], None, Color.GREEN, 0, (1710, 745)),
          Railroad("Short Line", action.land_on_property, 200, 25, None, (1710, 895)),
          Space("Chance", action.chance, (1710, 1045)),
          Home("Park Place", action.land_on_property, 350, [35, 175, 500, 1100, 1300, 1500], None, Color.DARK_BLUE, 0, (1710, 1195)),
          Space("Luxury Tax", action.luxury_tax, (1710, 1345)),
          Home("Boardwalk", action.land_on_property, 400, [50, 200, 600, 1400, 1710, 2000], None, Color.DARK_BLUE, 0, (1710, 1495)),
          ]


games = []
