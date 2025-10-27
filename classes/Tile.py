import pygame
import os
from config.config import tileSize, screen
tileTypeTextures = {
    "grass": "../media/grass.png",
    "stone": "../media/stone.png",
    "wood": "path",
    "wall": "path"
}

class Tile():
    def __init__(self, typee, wall, positionX, positionY):

        self.passable = not wall
        self.texture = tileTypeTextures[typee]
        self.posX = positionX
        self.posY = positionY

        texture_path = tileTypeTextures.get(typee)
        texture_path = os.path.join(os.path.dirname(__file__), texture_path)
        if texture_path and os.path.exists(texture_path):
            # Load and scale texture
            self.surface = pygame.image.load(texture_path).convert_alpha()
            self.surface = pygame.transform.scale(self.surface, (tileSize, tileSize))
        else:
            # fallback if missing
            self.surface = pygame.Surface((50, 50), pygame.SRCALPHA)
            self.surface.fill("blue")
        self.rect = self.surface.get_rect(topleft=(self.posX, self.posY))

    def draw(self, camera):
        screen.blit(self.surface, (self.posX - camera.offset_x, self.posY - camera.offset_y))