import random

from models import board
from models.properties import Home, Railroad, Utility


def land_on_property(current_player):
    current_space = board.games[0].players[board.games[0].current_player % len(board.games[0].players)].position
    property = board.games[0].spaces[current_space]
    owner = property.owner
    if owner is None:
        return "This property is unowned. Would you like to buy it? \n Use command $buy to buy this property. Otherwise, end your turn with $end turn"
    elif owner.name == current_player.name:
        return "You own this property"
    else:
        rent = rent_calculation(property)
        if current_player.adv_to_rail: 
            rent *= 2
            current_player.adv_to_rail = False
        elif current_player.roll_for_util:
            rent *= 10
            current_player.roll_for_util = False
        current_player.money -= rent
        owner.money += rent
        return f"This property is owned by {owner.name} and your rent costs ${rent}. Your new balance is ${current_player.money}"

def rent_calculation(property):
    rent = 0
    owner = property.owner
    if type(property) == Home:
        houses = property.houses # houses is 4 or less but 1 hotel = 5 houses
        color = property.color.value
        rent = property.rent[houses] # if there are no houses

        # owner.properties["homes"][color] is an array where [0] would be all the home groups in a specific color 
        # and [1] would be number of homes needed in the group color to be a full group
        # ie. if a player owned 2 brown homes, then this is a full set
        if len(owner.properties["homes"][color][0]) == owner.properties["homes"][color][1] and houses == 0:
            rent *= 2
        return rent
    elif type(property) == Railroad:
        rent = property.rent * pow(2, owner.railroads - 1)
    return rent


def collect_from_go(current_player):
    current_player.money += 200
    return f"{current_player.name} has passed GO and earned $200. Your new balance is ${current_player.money}"


def luxury_tax(current_player):
    current_player.money -= 100
    return f"{current_player.name} has paid $100 in luxury tax. Your new balance is ${current_player.money}"


def income_tax(current_player):
    current_player.money -= 200
    return f"{current_player.name} has paid $200 in luxury tax. Your new balance is ${current_player.money}"


def advance_to_boardwalk(current_player):
    current_player.position = 39
    current_player.new_space = True
    return "Advance to Boardwalk"


def advance_to_go(current_player):
    current_player.position = 0
    return f"Advance to Go (Collect $200). Your new balance is ${current_player.money}"


def advance_to_illinois(current_player):
    if current_player.position > 24:
        current_player.pass_go = True
    current_player.position = 24
    current_player.new_space = True
    return "Advance to Illinois Avenue. If you pass Go, collect $200"


def advance_to_stcharles(current_player):
    if current_player.position > 11:
        current_player.pass_go = True
    current_player.position = 11
    current_player.new_space = True
    return "Advance to St. Charles Place. If you pass Go, collect $200"


def advance_to_nearest_railroad(current_player):
    if current_player.position > 35:
        current_player.pass_go = True
    at_railroad = False
    while not at_railroad:
        if type(current_player.position) is not Railroad:
            current_player.position += 1
        else:
            at_railroad = True
    if current_player.position.owner and current_player.position.owner != current_player:
        current_player.adv_to_rail = True
    current_player.new_space = True
    return "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled"


def advance_to_nearest_utility(current_player):
    if current_player.position > 28:
        current_player.pass_go = True
    at_utility = False
    while not at_utility:
        if type(current_player.position) is not Utility:
            current_player.position += 1
        else:
            at_utility = True
    if current_player.position.owner  and current_player.position.owner != current_player:
        current_player.roll_for_util = True
    current_player.new_space = True
    current_player.roll = True
    return "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown."


def bank_paid_dividend(current_player):
    current_player.money += 50
    return f"Bank pays you dividend of $50. Your new balance is ${current_player.money}"


def get_out_of_jail_free(current_player):
    current_player.get_out_of_jail_free_cards += 1
    return "You have been given a 'Get Out of Jail Free' card"


def go_back_three(current_player):
    current_player.position -= 3
    current_player.new_space = True
    return "Go Back 3 Spaces"


def go_to_jail(current_player):
    current_player.position = 10
    current_player.in_jail = True
    return "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200"


def property_maintenance(current_player):
    current_player.money -= current_player.number_of_houses * 25
    current_player.money -= current_player.number_of_hotels * 100
    return f"Make general repairs on all your property. For each house pay $25. For each hotel pay $100. Your new balance is ${current_player.money}"


def speeding(current_player):
    current_player.money -= 15
    return f"Speeding fine $15. Your new balance is ${current_player.money}"


def trip_to_reading_railroad(current_player):
    if current_player.position > 5:
        current_player.pass_go = True
    current_player.position = 5
    return "Take a trip to Reading Railroad. If you pass Go, collect $200"


def selected_chairman(current_player):
    current_player.money -= (len(board.games[0].players) - 1) * 50
    for players in board.games[0].players:
        if players is current_player:
            pass
        else:
            board.games[0].players[players].money += 50
    return f"You have been elected Chairman of the Board. Pay each player $50. Your new balance is ${current_player.money}"


def mature_loan(current_player):
    current_player.money += 150
    return f"Your building loan matures. Collect $150. Your new balance is ${current_player.money}"


def bank_error(current_player):
    current_player.money += 200
    return f"Bank error in your favor. Collect $200. Your new balance is ${current_player.money}"


def doctor_fee(current_player):
    current_player.money -= 50
    return f"Doctor's fee. Pay $50. Your new balance is ${current_player.money}"


def sale_of_stock(current_player):
    current_player.money += 50
    return f"From sale of stock you get $50. Your new balance is ${current_player.money}"


def holiday_funds(current_player):
    current_player.money += 100
    return f"Holiday fund matures. Receive $100. Your new balance is ${current_player.money}"


def income_tax_refund(current_player):
    current_player.money += 20
    return f"Income tax refund. Collect $20. Your new balance is ${current_player.money}"


def your_birthday(current_player):
    birthday = 0
    for player in board.games[0].players:
        birthday += 10
        player.money -= 10
    current_player.money = birthday
    return f"It is your birthday. Collect $10 from every player. Your new balance is ${current_player.money}"


def life_insurance(current_player):
    current_player.money += 100
    return f"Life insurance matures. Collect $100. Your new balance is ${current_player.money}"


def hospital_fees(current_player):
    current_player.money -= 100
    return f"Pay hospital fees of $100. Your new balance is ${current_player.money}"


def school_fees(current_player):
    current_player.money -= 50
    return f"Pay school fees of $50. Your new balance is ${current_player.money}"


def consultancy(current_player):
    current_player.money += 25
    return f"Receive $25 consultancy fee. Your new balance is ${current_player.money}"


def street_repair(current_player):
    current_player.money -= current_player.number_of_houses * 40
    current_player.money -= current_player.number_of_hotels * 115
    return f"You are assessed for street repair. $40 per house. $115 per hotel. Your new balance is ${current_player.money}"


def beauty(current_player):
    current_player.money += 10
    return f"You have won second prize in a beauty contest. Collect $10. Your new balance is ${current_player.money}"


def inheritance(current_player):
    current_player.money += 100
    return f"You inherit $100. Your new balance is ${current_player.money}"


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
    card_pick = 1
    # random.randint(0, len(chance_cards) - 1)
    return chance_cards[card_pick](current_player)


def community_chest(current_player):
    card_pick = 1
    # random.randint(0, len(community_chest_cards) - 1)
    return community_chest_cards[card_pick](current_player)


def free_parking(current_player):
    return "You are in free parking"


def prison(current_player):
    return "You are just visiting"
