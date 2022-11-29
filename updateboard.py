import nextcord
from PIL import Image
from models.board import games

# creating the board

def create_board():
    img = Image.open("boardimg.jpg") # img size is 1920 by 1920
    img = img.save("gameboard.jpg")
    
    file = nextcord.File("boardimg.jpg", filename="boardimg.jpg")
    embed = nextcord.Embed()
    embed.set_image(url="attachment://boardimg.jpg")

    return file, embed

def join_board(player):
    boardimg = Image.open("gameboard.jpg") # img size is 1920 by 1920
    boardimgbackground = boardimg.copy()

    piece = Image.open(f"models/pieceimgs/{player.character}.png")
    
    boardimgbackground.paste(piece, (player.characterx, player.charactery))
    boardimgbackground.save("gameboard.jpg", quality=95)

    
    file = nextcord.File("gameboard.jpg", filename="gameboard.jpg")
    embed = nextcord.Embed()
    embed.set_image(url="attachment://gameboard.jpg")
    
    return file, embed

def update_board():

    allplayers = games[0].players
    allspaces = games[0].spaces
    img = Image.open("boardimg.jpg") # img size is 1920 by 1920
    boardimgbackground = img.copy()

    for player in allplayers:
        image = Image.open(f"models/pieceimgs/{player.character}.png")
        boardimgbackground.paste(image, (player.characterx, player.charactery))

    boardimgbackground.save("gameboard.jpg", quality=95)

    file = nextcord.File("gameboard.jpg", filename="gameboard.jpg")
    embed = nextcord.Embed()
    embed.set_image(url="attachment://gameboard.jpg")

    return file, embed