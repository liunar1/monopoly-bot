import nextcord
from nextcord import PartialMessage
from models import player
from models import properties
from models import board


def land_on_property(current_player):
    if board.board is None:
        return
    else:
        if board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].owner is None:
            return "unowned"
        else:
            current_player.money -= board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].rent
            board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].owner.money += board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].rent
