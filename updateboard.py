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

    num_houses = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five"
    }

    def possessions(player, image, property_type: str):
        if property_type == "homes":
            for colors in player.properties[property_type]: # going through each color
                for pos in player.properties[property_type][colors][0]: # positions in sublist of sublist
                    property = games[0].spaces[pos]
                    boardimgbackground.paste(image, (property.own_coords))
                    if property.houses:
                        house_number = Image.open(f"models/pieceimgs/{num_houses[property.houses]}.png")
                        house_number = house_number.resize((house_number.width, house_number.height))
                        boardimgbackground.paste(house_number, (property.house_coords))
        else:
            for pos in player.properties[property_type]:
                boardimgbackground.paste(image, (games[0].spaces[pos].own_coords))

    for player in allplayers:
        image = Image.open(f"models/pieceimgs/{player.character}.png")
        boardimgbackground.paste(image, (player.characterx, player.charactery))
        ownerimage = Image.open(f"models/pieceimgs/{player.character}house.png")
        ownerimage = ownerimage.resize((ownerimage.width // 2, ownerimage.height // 2))
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