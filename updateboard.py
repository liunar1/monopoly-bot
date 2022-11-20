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

def join_board():

    boardimg = Image.open("gameboard.jpg") # img size is 1920 by 1920
    boardimgbackground = boardimg.copy()

    boardimgbackground.save("gameboard.jpg", quality=95)

    file = nextcord.File("gameboard.jpg", filename="gameboard.jpg")
    embed = nextcord.Embed()
    embed.set_image(url="attachment://gameboard.jpg")

    return file, embed

def update_board():
    img = Image.open("boardimg.jpg") # img size is 1920 by 1920
    img = img.save("gameboard.jpg")

    boardimg = Image.open("gameboard.jpg")
    boardimgbackground = boardimg.copy()

    boardimgbackground.save("gameboard.jpg", quality=95)

    file = nextcord.File("gameboard.jpg", filename="gameboard.jpg")
    embed = nextcord.Embed()
    embed.set_image(url="attachment://gameboard.jpg")

    return file, embed