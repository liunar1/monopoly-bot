import nextcord
from nextcord.ext import commands
from time import sleep
from models.board import Board, games
from models.player import Player
from action import collect_from_go, land_on_property
from models.properties import Home, Railroad, Utility
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
        if games[0]:
            await ctx.send('Sorry, there\'s already a game occuring')
        return
    except:
        # if num_players < 2 or num_players > 8:
        #     await ctx.reply('Invalid number of players. There must be 2 - 8 players per game')
        #     return
        games.append(Board(num_players))
        file, embed = create_board()
        await ctx.send(file=file, embed=embed)
        await ctx.send(f'Game has been created for {games[0].num_players} players')
        await ctx.send(f'Here are the available characters: \nairplane, boat, car, dog, hat, magnet, can, shoe')


@create.error
async def create_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('Please indicate number of players!')
    else:
        await ctx.reply('What are you doing?!')
        

@bot.command()
async def join(ctx, character: str):
    # the first if statement will throw an error to the def join(ctx, error) function
    if games[0].characters:
        pass
    if character not in games[0].characters:
        await ctx.reply('That character doesn\'t exist!')
        return
    try:
        games[0].characters.remove(character)
    except:
        await ctx.reply('Sorry. That character is already taken. Please pick something else!')
        return
    if len(games[0].players) >= games[0].num_players:
        await ctx.reply(f'Sorry, the game is now full')
    else:
        for player in games[0].players:
            if player.name == ctx.author:
                await ctx.reply('You are already in this game!')
                return
        # player arguments: player name, character, starting balance ($), number of houses, hotels, and get of jail cards
        current_player = Player(ctx.author, character, 1500, 0, 0, 0)
        games[0].players.append(current_player)
        file, embed = join_board(current_player)

        await ctx.send(file=file, embed=embed)
        await ctx.send(f'{ctx.author} has joined the game as {character}')

        if len(games[0].players) == games[0].num_players:
            await ctx.send('Game is now full. Let\'s play!')


@join.error
async def join(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('Please indicate the character you want to be!')
    else:
        await ctx.reply('You cannot join a nonexistent game!')


@bot.command()
async def roll(ctx):
    try:
        player = games[0].players[games[0].current_player]
    except:
        await ctx.reply('You are not in a game!')
        return
    if ctx.author == player.name:
        if not player.roll:
            await ctx.reply('You can\'t roll again!')
        else:
            player.roll = False
            await ctx.send(f'{ctx.author} has rolled a {player.rolling(player)}!')
            sleep(2)
            player = games[0].players[games[0].current_player]
            if player.roll_for_util:
                await ctx.reply(land_on_property(player))
            elif player.in_jail:
                if player.double_roll_ct:
                    await ctx.send(f'{ctx.author} has rolled a double!')
                    await ctx.reply('You are now free from jail')
                    player.in_jail = False
                    current_position = games[0].spaces[player.position]
                    await ctx.reply(f'You are now on {current_position.name}')
                else:
                    await ctx.send(f'{ctx.author} did not roll a double and is still in jail')
            else:
                current_position = games[0].spaces[player.position]
                await ctx.reply(f'You are now on {current_position.name}')
                await ctx.reply(current_position.action(player))
            if player.pass_go:
                await ctx.send(collect_from_go(player))
                player.pass_go = False
            if player.new_space:
                await ctx.reply(land_on_property(player))
                player.new_space = False
        file, embed = update_board()

        await ctx.send(file=file, embed=embed)
    else:
        await ctx.reply('Sorry, it\'s not your turn')

@bot.command()
async def buy(ctx, *args):
    current_player = games[0].players[games[0].current_player]
    if type(games[0].spaces[current_player.position]) != Home and type(games[0].spaces[current_player.position]) != Utility and type(games[0].spaces[current_player.position]) != Railroad:
        await ctx.reply('You can\'t buy a non property!')
        return
    property = games[0].spaces[current_player.position]
    # initially buying the property
    if not len(args): 
        if not property.owner:
            current_player.buy(current_player, property)
            await ctx.send(f'{ctx.author} has bought {property.name}! Your new balance is ${current_player.money}')
        else: 
            await ctx.reply('This property is owned!')
        return
    # buying a house / hotel
    if current_player.position.owner != current_player:
        await ctx.reply('This property is not yours!')
        return
    else:
        if args[0] == 'house':
            current_player.buy_house(property)
            await ctx.send(f'{ctx.author} has bought a house on {property.name}!')
        elif args[0] == 'hotel':
            current_player.buy_hotel(property)
            await ctx.send(f'{ctx.author} has bought a hotel on {property.name}!')
        else:
            await ctx.send(f'{args[0]} is not purchasable!')


@bot.command()
async def end(ctx):
    player = games[0].players[games[0].current_player]
    if ctx.author == player.name:
        if player.money < 0:
            if not player.confirm_bankrupt:
                player.confirm_bankrupt = True
                await ctx.reply('You are currently in debt. If you do $end, you will automatically be forced into bankruptcy. Confirm the command once again if this is your decision')
                return
            else:
                # unfinished command
                if len(games[0].players) == 1:
                    games[0].current_player += 1 
                    games[0].current_player %= len(games[0].players)
                    await ctx.send(f'Congratulations {games[0].players[games[0].current_player].name}! You won the game!')
                    await ctx.send('The game is now over. Please start a new game')
                    games.pop()
                    return
        await ctx.send(f'{ctx.author}\'s turn has ended')
        games[0].current_player += 1 
        games[0].current_player %= len(games[0].players)
        games[0].players[games[0].current_player].roll = True
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
        await ctx.send(f'{ctx.author} has sold {property.name}!')

@bot.command()
async def free(ctx):
    current_player = games[0].players[games[0].current_player]
    if current_player.get_out_of_jail_free_cards:
        current_player.get_out_of_jail_free_cards -= 1
        await ctx.send(f'{ctx.author} is free from jail!')
    else:
        await ctx.reply('Sorry, you don\'t have any cards that can get you out of jail')

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
