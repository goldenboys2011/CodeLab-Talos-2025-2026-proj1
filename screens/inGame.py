from config.config import mapHeight, mapWidth,tileSize
from classes.Tile import Tile
import random
from ui.Image import Image
#from ui.Rectangle import Rectangle

# == Tile setup ==
grassFloor = []

for i in range(0, mapWidth):
    for j in range(0,mapHeight):
        if random.randint(0, 1) >= 0.2 : tile = "grass" 
        else: tile = "path"
        grassFloor.append(Tile(tile, False, i * tileSize, j * tileSize))

# == In Game UI ==
UI = []

UI.append(Image("./media/skull.png", 0, 0, 120, 120))