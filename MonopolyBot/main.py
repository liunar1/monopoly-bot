from nextcord.ext import commands
from nextcord import User
from models import board
from models.player import Player
from models import properties

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
    # print(f"{len(board.board.players)} is how  many people joined the game")


@client.command()  # currently for testing purposes only
async def delete_board(ctx):
    board.board = None
    await ctx.reply("Game has been deleted")
    print("Game has been deleted")


@client.command() # also probably for testing purposes only, will I need this during actual use?
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
    await ctx.reply(f"{Player.name} rolled a {Player.rolling()}!")  # could use some help here
    Player.position += Player.position
    await ctx.send(f"{Player.name}'s position is {Player.position}")


@client.command()
async def buy(ctx):
    await ctx.reply(f"{Player.name} bought the property")
    # I want to change this in the future so that I can indicate which property has been bought


client.run('ODE4MjE2NTI2ODYzMjY5OTA4.YEU1hQ.5evOHgwKAtzdRGMMXfNgSQew6Cc')
