import random

from models import board
from models.properties import Home, Railroad, Utility


def land_on_property(current_player):
    current_space = board.games[0].players[board.games[0].current_player % len(board.games[0].players)].position
    property = board.games[0].spaces[current_space]
    owner = property.owner
    if board.games[0] is None:
        return
    else:
        if owner is None:
            return "This property is unowned. Would you like to buy it?"
        else:
            rent = rent_calculation(property)
            current_player.money -= rent
            owner.money += rent
            return f"This property is owned by {owner.name} and your rent costs ${rent}. Your new balance is ${current_player.money}"

def rent_calculation(property):
    rent = 0
    owner = property.owner
    if type(property) == Home:
        houses = property.houses # houses is 4 or less but 1 hotel = 5 houses
        color = property.color
        rent = property.rent[houses] # if there are no houses

        # owner.homes[color] is an array where [0] would be all the home groups in a specific color 
        # and [1] would be number of homes needed in the group color to be a full group
        # ie. if a player owned 2 brown homes, then this is a full set
        if len(owner.homes[color][0]) == owner.homes[color][1]:
            rent *= 2
    elif type(property) == Railroad:
        rent = property.rent * pow(2, owner.railroads - 1)
    return rent
    

def new_balance(current_player):
    return f"Your new balance is ${current_player.money}"


def collect_from_go(current_player):
    if board.games[0] is None:
        return
    else:
        current_player.money += 200
        return f"{current_player.name} has passed GO and earned $200. Your new balance is ${current_player.money}"


def luxury_tax(current_player):
    if board.games[0] is None:
        return
    else:
        current_player.money -= 100
        return f"{current_player.name} has paid $100 in luxury tax. Your new balance is ${current_player.money}"


def income_tax(current_player):
    if board.games[0] is None:
        return
    else:
        current_player.money -= 200
        return f"{current_player.name} has paid $200 in luxury tax. Your new balance is ${current_player.money}"


def advance_to_boardwalk(current_player):
    current_player.position = 39
    return "Advance to Boardwalk"


def advance_to_go(current_player):
    current_player.position = 0
    current_player.new_balance = True
    return "Advance to Go (Collect $200)"


def advance_to_illinois(current_player):
    pass_go = None
    if current_player.position > 24:
        pass_go = True
    current_player.position = 24
    return "Advance to Illinois Avenue. If you pass Go, collect $200"


def advance_to_stcharles(current_player):
    pass_go = None
    if current_player.position > 11:
        pass_go = True
    current_player.position = 11
    return "Advance to St. Charles Place. If you pass Go, collect $200"


def advance_to_nearest_railroad(current_player):
    pass_go = None
    if current_player.position > 35:
        pass_go = True
    at_railroad = False
    while not at_railroad:
        if type(current_player.position) is not Railroad:
            current_player.position += 1
        else:
            at_railroad = True
    return "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled"


def advance_to_nearest_utility(current_player):
    pass_go = None
    if current_player.position > 28:
        pass_go = True
    at_utility = False
    while not at_utility:
        if type(current_player.position) is not Utility:
            current_player.position += 1
        else:
            at_utility = True
    return "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown."


def bank_paid_dividend(current_player):
    current_player.money += 50
    current_player.new_balance = True
    return "Bank pays you dividend of $50"


def get_out_of_jail_free(current_player):
    current_player.get_out_of_jail_free_cards += 1
    return "Get Out of Jail Free"


def go_back_three(current_player):
    current_player.position -= 3
    return "Go Back 3 Spaces"


def go_to_jail(current_player):
    current_player.position = 10
    return "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200"


def property_maintenance(current_player):
    current_player.money -= current_player.number_of_houses * 25
    current_player.money -= current_player.number_of_hotels * 100
    current_player.new_balance = True
    return "Make general repairs on all your property. For each house pay $25. For each hotel pay $100"


def speeding(current_player):
    current_player.money -= 15
    current_player.new_balance = True
    return "Speeding fine $15"


def trip_to_reading_railroad(current_player):
    pass_go = None
    if current_player.position > 5:
        pass_go = True
    current_player.position = 5
    return "Take a trip to Reading Railroad. If you pass Go, collect $200"


def selected_chairman(current_player):
    current_player.money -= (len(board.games[0].players) - 1) * 50
    for players in board.games[0].players:
        if players is current_player:
            pass
        else:
            board.games[0].players[players].money += 50
    current_player.new_balance = True
    return "You have been elected Chairman of the Board. Pay each player $50"


def mature_loan(current_player):
    current_player.money += 150
    current_player.new_balance = True
    return "Your building loan matures. Collect $150"


def bank_error(current_player):
    current_player.money += 200
    current_player.new_balance = True
    return "Bank error in your favor. Collect $200"


def doctor_fee(current_player):
    current_player.money -= 50
    current_player.new_balance = True
    return "Doctor's fee. Pay $50"


def sale_of_stock(current_player):
    current_player.money += 50
    current_player.new_balance = True
    return "From sale of stock you get $50"


def holiday_funds(current_player):
    current_player.money += 100
    current_player.new_balance = True
    return "Holiday fund matures. Receive $100"


def income_tax_refund(current_player):
    current_player.money += 20
    current_player.new_balance = True
    return "Income tax refund. Collect $20"


def your_birthday(current_player):
    current_player.new_balance = True
    return "It is your birthday. Collect $10 from every player"


def life_insurance(current_player):
    current_player.money += 100
    current_player.new_balance = True
    return "Life insurance matures. Collect $100"


def hospital_fees(current_player):
    current_player.money -= 100
    current_player.new_balance = True
    return "Pay hospital fees of $100"


def school_fees(current_player):
    current_player.money -= 50
    current_player.new_balance = True
    return "Pay school fees of $50"


def consultancy(current_player):
    current_player.money += 25
    current_player.new_balance = True
    return "Receive $25 consultancy fee"


def street_repair(current_player):
    current_player.money -= current_player.number_of_houses * 40
    current_player.money -= current_player.number_of_hotels * 115
    current_player.new_balance = True
    return f"You are assessed for street repair. $40 per house. $115 per hotel."


def beauty(current_player):
    current_player.money += 10
    current_player.new_balance = True
    return "You have won second prize in a beauty contest. Collect $10"


def inheritance(current_player):
    current_player.money += 100
    current_player.new_balance = True
    return "You inherit $100"


chance_cards = [
    advance_to_boardwalk,
    advance_to_go,
    advance_to_illinois,
    advance_to_stcharles,
    advance_to_nearest_railroad,
    advance_to_nearest_utility,
    bank_paid_dividend,
    get_out_of_jail_free,
    go_back_three,
    go_to_jail,
    property_maintenance,
    speeding,
    trip_to_reading_railroad,
    selected_chairman,
    mature_loan
]

community_chest_cards = [
    advance_to_go,
    bank_error,
    doctor_fee,
    sale_of_stock,
    get_out_of_jail_free,
    go_to_jail,
    holiday_funds,
    income_tax_refund,
    your_birthday,
    life_insurance,
    hospital_fees,
    school_fees,
    consultancy,
    street_repair,
    beauty,
    inheritance
]


def chance(current_player):
    if board.games[0] is None:
        return
    else:
        card_pick = random.randint(0, len(chance_cards) - 1)
        chance_cards[card_pick](current_player)


def community_chest(current_player):
    if board.games[0] is None:
        return
    else:
        card_pick = random.randint(0, len(community_chest_cards) - 1)
        return community_chest_cards[card_pick](current_player)


def jailed(current_player):
    current_player.position = 10


def free_parking(current_player):
    pass


def prison(current_player):
    return "You are just visiting"
