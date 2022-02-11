from nextcord.ext import commands
from models.board import board
# from models.board import Board
from models.player import Player

client = commands.Bot(command_prefix='$')

list_of_players = []


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def ping(ctx):
    await ctx.reply('Pong!')
    await ctx.send('ctx works again')


@client.command()
async def create_game(ctx, number_of_players):
    # if board.board is not None:
    #     await ctx.reply("Game already in progress you fucking clown!")
    #     return
    # board.board = board.Board(2)
    await ctx.reply(f'Game is starting with {number_of_players} players')
    # await ctx.reply(f'The first property on the board is {board.board.spaces[0]}')


@client.command()
async def join(ctx):
    list_of_players.append(Player(Player.name, 1500, 0))
    await ctx.reply(f"{Player.name} has joined the game.")


@client.command()
async def roll(ctx):
    await ctx.reply(f"{Player.name} rolled a {Player.rolling()}!")  # could use some help here
    Player.position += Player.position
    await ctx.send(f"{Player.name}'s position is {Player.position}")


@client.command()
async def buy(ctx):
    await ctx.reply(f"{Player.name} bought the property")
    # I want to change this in the future so that I can indicate which property has been bought


current_turn = 0
if Player.position == 4:
    list_of_players[current_turn].tax(200)
if Player.position == 39:
    list_of_players[current_turn].tax(100)

client.run('ODE4MjE2NTI2ODYzMjY5OTA4.YEU1hQ.5evOHgwKAtzdRGMMXfNgSQew6Cc')
