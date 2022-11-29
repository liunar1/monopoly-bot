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

    def possessions(player, image, property: str):
        if property == "homes":
            for colors in player.properties[property]: # going through each color
                for pos in player.properties[property][colors][0]: # positions in sublist of sublist
                    boardimgbackground.paste(image, (games[0].spaces[pos].house_coords))
        else:
            for pos in player.properties[property]:
                boardimgbackground.paste(image, (games[0].spaces[pos].house_coords))

    for player in allplayers:
        image = Image.open(f"models/pieceimgs/{player.character}.png")
        boardimgbackground.paste(image, (player.characterx, player.charactery))
        ownerimage = Image.open(f"models/pieceimgs/{player.character}house.png")
        if player.properties:
            possessions(player, ownerimage, "homes")
        if player.railroads:
            possessions(player, ownerimage, "railroads")
        if player.utilities:
            possessions(player, ownerimage, "utilities")

    boardimgbackground.save("gameboard.jpg", quality=95)

    file = nextcord.File("gameboard.jpg", filename="gameboard.jpg")
    embed = nextcord.Embed()
    embed.set_image(url="attachment://gameboard.jpg")

    return file, embed