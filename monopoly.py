import nextcord
from nextcord.ext import commands
from time import sleep
from models.board import Board, games
from models.player import Player
from action import collect_from_go, new_balance
from updateboard import create_board, join_board, update_board

intents = nextcord.Intents.all()
intents.message_content = True # this is to allow the bot to send messages
bot = commands.Bot(command_prefix='$', intents=intents) # $ goes before every command

# event will run when the bot is online
@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command()
async def create(ctx, num_players: int):
    try:
        if games:
            await ctx.send('Sorry, there\'s already a game occuring')
            return
    except:
        # if num_players < 2 or num_players > 8:
        #     await ctx.reply('Invalid number of players. There must be 2 - 8 players per game')
        #     return
        games = Board(num_players)
        file, embed = create_board()
        await ctx.send(file=file, embed=embed)
        await ctx.send(f'Game has been created for {games.num_players} players')
        await ctx.send(f'Here are the available characters: \nairplane, boat, car, dog, hat, magnet, can, shoe')
        

@bot.command()
async def join(ctx, character):
    # try:
    games.characters.remove(character)
    # except:
    #     await ctx.reply('Sorry. That character is already taken. Please pick something else!')
    #     return
    if len(games.players) >= games.num_players:
        await ctx.reply(f'Sorry, the game is now full')
        return
    # player arguments: player name, character, starting balance ($), number of houses, hotels, and get of jail cards
    games.players.append(Player(ctx.author, character, 1500, 0, 0, 0))
    await ctx.send(f'{ctx.author} has joined the game as {character}')
    if len(games.players) == games.num_players:
        await ctx.send('Game is now full. Let\'s play!')
        

@bot.command()
async def roll(ctx):
    player = games[0].players[games[0].current_player]
    if ctx.author == player.name:
        await ctx.send(f'{ctx.author} has rolled a {player.rolling(player)}!')
        current_position = games[0].spaces[player.position]
        if player.pass_go:
            collect_from_go(player)
            player.pass_go = False
        sleep(2)
        await ctx.reply(f'You are now on {current_position.name}')
        # try:
        await ctx.reply(current_position.action(player))
        # except:
        #     print('space has no action / error')
        #     pass
        if player.new_balance:
            await ctx.reply(f'Your new balance is {player.money}')
            player.new_balance = False
        if player.pass_go:
            await ctx.reply(collect_from_go)
            player.pass_go = False
    else:
        await ctx.reply('Sorry, it\'s not your turn')

@bot.command()
async def buy(ctx, *args):
    current_player = games[0].players[games[0].current_player]
    # initially buying the property
    if not len(args):
        current_player.buy(current_player, games[0].spaces[current_player.position])
        await ctx.send(f'{ctx.author} has bought {games[0].spaces[current_player.position].name}!')
        await ctx.reply(new_balance(current_player))
        return
        # buying a house / hotel
    if args[0] == 'house':
        current_player.buy_house(games[0].spaces[current_player.position])
        await ctx.send(f'{ctx.author} has bought a house on {games[0].spaces[current_player.position].name}!')
    elif args[0] == 'hotel':
        current_player.buy_hotel(games[0].spaces[current_player.position])
        await ctx.send(f'{ctx.author} has bought a hotel on {games[0].spaces[current_player.position].name}!')
    else:
        current_player.buy_hotel(games[0].spaces[current_player.position])
        await ctx.send(f'{args[0]} is not purchasable!')

@bot.command()
async def free(ctx): # free from jail
    pass

@bot.command()
async def end(ctx):
    if ctx.author == games[0].players[games[0].current_player].name:
        await ctx.send(f'{ctx.author}\'s turn has ended')
        games[0].current_player += 1 
        games[0].current_player %= len(games[0].players)
        await ctx.send('Here\'s an update on the properties: ')
        await ctx.send(f'It is now {games[0].players[games[0].current_player].name}\'s turn')
    else:
        await ctx.reply('Sorry, it\'s not your turn')

@bot.command()
async def sell(ctx, *args):
    current_player = games[0].players[games[0].current_player]
    property = games[0].spaces[current_player.position]
    if args[0] == 'house':
        current_player.buy_house(property)
        await ctx.send(f'{ctx.author} has sold a house on {property.name}!')
    elif args[0] == 'hotel':
        current_player.buy_hotel(property)
        await ctx.send(f'{ctx.author} has sold a hotel on {property.name}!')
    else:
        await ctx.send(f'{ctx.author} have sold {property.name}!')

@bot.command()
async def mortgage(ctx):
    pass

@bot.command()
async def bankrupt(ctx):
    await ctx.send(f'{ctx.author} has declared bankruptcy')
    games[0].players.pop(games[0].current_player)
    if len(games[0].players) == 1:
        await ctx.send(f'Congratulations {games[0].players[games[0].current_player].name}! You won the game!')
        await ctx.send('The game is now over. Please start a new game')
        games.pop()
        return
    await ctx.send(f'It is now {games[0].players[games[0].current_player].name}\'s turn')

bot.run('ODE4MjE2NTI2ODYzMjY5OTA4.Ga9Dd-.qEIbtbUPec4vrLgbZ7sfkBo_0jUuqDh2a5uUZg')
