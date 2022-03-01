from nextcord.ext import commands
from nextcord import User
from models import board
from models.player import Player
from models import properties
import action

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def create_game(ctx, number_of_players):
    if board.board is not None:
        await ctx.reply("Game already in progress you fucking clown!")
        return
    board.board = board.Board(number_of_players)
    await ctx.reply(f'Game is starting with {number_of_players} players')
    await ctx.reply(f'The first property on the board is {board.board.spaces[0].name}')
    # print(f"{board.board.num_players} is how many people are in the current game")
    # print(f"{len(board.board.players)} is current length of player list")


@client.command()
async def join(ctx):
    if board.board is None:
        await ctx.reply("Bro there's not even a game created stupidass")
        return
    in_game = False
    for i in board.board.players:
        if i.name == ctx.author:
            in_game = True
    if len(board.board.players) < int(board.board.num_players):
        if in_game:
            await ctx.reply("You are already in the game. You can't join it again you fucking clown!")
        else:
            board.board.players.append(Player(ctx.author, 1500, 0))
            await ctx.reply(f"{board.board.players[len(board.board.players) - 1].name} has joined the game.")
    else:
        await ctx.reply("Sorry, but the game is full. Please go find more friends to create a new game.")
    if len(board.board.players) == int(board.board.num_players):
        board.board.currentPlayer = 0
        await ctx.reply(
            f"The game is now full. {board.board.players[board.board.currentPlayer].name} will take the first turn.")

    # print(f"{len(board.board.players)} is how  many people joined the game")


@client.command()  # currently for testing purposes only
async def delete_game(ctx):
    board.board = None
    await ctx.reply("Game has been deleted")
    print("Game has been deleted")


@client.command()  # also probably for testing purposes only, will I need this during actual use?
async def check(ctx):
    in_game = False
    for i in board.board.players:
        # print(i.name)
        # print(ctx.author)
        if i.name == ctx.author:
            in_game = True
    if in_game:
        await ctx.reply("You are in this game.")
    else:
        await ctx.reply("You're not in this game. Please go find more friends to create a new game.")


@client.command()
async def roll(ctx):
    if board.board is None:
        await ctx.reply("What the fuck you're not even in the game stop trying to roll the dice")
        return
    in_game = False
    for i in board.board.players:
        if i.name == ctx.author:
            in_game = True
    if in_game is False:
        await ctx.reply("What the fuck you're not even in the game stop trying to roll the dice")
    else:
        if board.board.players[board.board.currentPlayer % len(board.board.players)].name == ctx.author:
            await ctx.reply(
                f"You rolled a {board.board.players[board.board.currentPlayer % len(board.board.players)].rolling()}!")
            await ctx.send(
                f"{board.board.players[board.board.currentPlayer % len(board.board.players)].name} has now landed on {board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].name}")
            if board.board.spaces[
                board.board.players[board.board.currentPlayer % len(board.board.players)].position].action(
                    board.board.players[board.board.currentPlayer % len(board.board.players)]) == "unowned":
                buyable()
                await ctx.reply(
                    f"This property is unowned. Would you like to buy it for ${board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].cost}?")
            else:
                await ctx.reply(
                    f"This property is owned by {board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].owner.name}")
                await ctx.send(
                    f"{board.board.players[board.board.currentPlayer % len(board.board.players)].name} has paid {board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].owner.name} ${board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].rent} for rent")
                await ctx.reply(f"Your new balance is ${board.board.players[board.board.currentPlayer % len(board.board.players)].money}")
        else:
            await ctx.reply("Bro stop trying to roll it's not even your fucking turn")


def buyable():
    return True


@client.command()
async def buy(ctx):
    if ctx.author == board.board.players[board.board.currentPlayer % len(board.board.players)].name and buyable:
        board.board.spaces[
            board.board.players[board.board.currentPlayer % len(board.board.players)].position].owner = \
        board.board.players[board.board.currentPlayer % len(board.board.players)]
        board.board.players[board.board.currentPlayer % len(board.board.players)].money -= board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].cost
        await ctx.reply(
            f"Congratulations! You now own {board.board.spaces[board.board.players[board.board.currentPlayer % len(board.board.players)].position].name}. Your new balance is {board.board.players[board.board.currentPlayer % len(board.board.players)].money}")


@client.command()
async def endturn(ctx):
    if ctx.author == board.board.players[board.board.currentPlayer % len(board.board.players)].name:
        board.board.currentPlayer += 1
        await ctx.send(
            f"It is now {board.board.players[board.board.currentPlayer % len(board.board.players)].name}'s turn.")


client.run('ODE4MjE2NTI2ODYzMjY5OTA4.YEU1hQ.5evOHgwKAtzdRGMMXfNgSQew6Cc')
