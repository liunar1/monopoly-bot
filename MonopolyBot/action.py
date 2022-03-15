from models.properties import Railroad
from models.properties import Utility
from models import board
import random


def land_on_property(current_player):
    if board.board is None:
        return
    else:
        if board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)]
                .position].owner is None:
            return "unowned"
        else:
            current_player.money -= board.board.spaces[
                board.board.players[board.board.currentPlayer % len(board.board.players)].position].rent
            board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].owner.money += \
                board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].rent


def collect_from_go(current_player):
    if board.board is None:
        return
    else:
        current_player.money += 200
        return f"{current_player.name} has passed GO and earned $200. Your new balance is ${current_player.money}"


def luxury_tax(current_player):
    if board.board is None:
        return
    else:
        current_player.money -= 100
        return f"{current_player.name} has paid $100 in luxury tax. Your new balance is ${current_player.money}"


def income_tax(current_player):
    if board.board is None:
        return
    else:
        current_player.money -= 200
        return f"{current_player.name} has paid $200 in luxury tax. Your new balance is ${current_player.money}"


def advance_to_boardwalk(current_player):
    current_player.position = 39
    return "Advance to Boardwalk", True, False, True


def advance_to_go(current_player):
    current_player.position = 0
    return "Advance to Go (Collect $200)", True, True, False


def advance_to_illinois(current_player):
    pass_go = None
    if current_player.position > 24:
        pass_go = True
    current_player.position = 24
    return "Advance to Illinois Avenue. If you pass Go, collect $200", True, pass_go, True


def advance_to_stcharles(current_player):
    pass_go = None
    if current_player.position > 11:
        pass_go = True
    current_player.position = 11
    return "Advance to St. Charles Place. If you pass Go, collect $200", True, pass_go, True


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
    return "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled", True, pass_go, True


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
    return "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.", True, pass_go, True


def bank_paid_dividend(current_player):
    current_player.money += 50
    return "Bank pays you dividend of $50", False, True, False


def get_out_of_jail_free(current_player):
    current_player.get_out_of_jail_free_cards += 1
    return "Get Out of Jail Free", False, False, False


def go_back_three(current_player):
    current_player.position -= 3
    return "Go Back 3 Spaces", True, False, True


def go_to_jail(current_player):
    current_player.position = 10
    return "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200", True, False, False


def property_maintenance(current_player):
    current_player.money -= current_player.number_of_houses * 25
    current_player.money -= current_player.number_of_hotels * 100
    return "Make general repairs on all your property. For each house pay $25. For each hotel pay $100", False, True, False


def speeding(current_player):
    current_player.money -= 15
    return "Speeding fine $15", False, True, False


def trip_to_reading_railroad(current_player):
    pass_go = None
    if current_player.position > 5:
        pass_go = True
    current_player.position = 5
    return "Take a trip to Reading Railroad. If you pass Go, collect $200", True, pass_go, True


def selected_chairman(current_player):
    current_player.money -= (len(board.board.players) - 1) * 50
    for players in board.board.players:
        if players is current_player:
            pass
        else:
            board.board.players[players].money += 50
    return "You have been elected Chairman of the Board. Pay each player $50", False, True, False


def mature_loan(current_player):
    current_player.money += 150
    return "Your building loan matures. Collect $150", False, True, False


def bank_error(current_player):
    current_player.money += 200
    return "Bank error in your favor. Collect $200", False, True, False


def doctor_fee(current_player):
    current_player.money -= 50
    return "Doctor’s fee. Pay $50", False, True, False


def sale_of_stock(current_player):
    current_player.money += 50
    return "From sale of stock you get $50", False, True, False


def holiday_funds(current_player):
    current_player.money += 100
    return "Holiday fund matures. Receive $100", False, True, False


def income_tax_refund(current_player):
    current_player.money += 20
    return "Income tax refund. Collect $20", False, True, False


def your_birthday(current_player):
    return "It is your birthday. Collect $10 from every player", False, True, False


def life_insurance(current_player):
    current_player.money += 100
    return "Life insurance matures. Collect $100", False, True, False


def hospital_fees(current_player):
    current_player.money -= 100
    return "Pay hospital fees of $100", False, True, False


def school_fees(current_player):
    current_player.money -= 50
    return "Pay school fees of $50", False, True, False


def consultancy(current_player):
    current_player.money += 25
    return "Receive $25 consultancy fee", False, True, False


def street_repair(current_player):
    current_player.money -= current_player.number_of_houses * 40
    current_player.money -= current_player.number_of_hotels * 115
    return "You are assessed for street repair. $40 per house. $115 per hotel", False, True, False


def beauty(current_player):
    current_player.money += 10
    return "You have won second prize in a beauty contest. Collect $10", False, True, False


def inheritance(current_player):
    current_player.money += 100
    return "You inherit $100", False, True, False


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
    if board.board is None:
        return
    else:
        card_pick = random.randint(0, len(chance_cards) - 1)
        chance_cards[card_pick](current_player)


def community_chest(current_player):
    if board.board is None:
        return
    else:
        card_pick = random.randint(0, len(community_chest_cards) - 1)
        return community_chest_cards[card_pick](current_player)


def jailed(current_player):
    current_player.position = 10


def free_parking(current_player):
    pass


def prison(current_player):
    pass
