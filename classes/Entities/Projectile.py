import pygame
from config.config import tileSize, screen

class Projectile():
    def __init__(self, speed, strength, texture, posX, posY):
        self.strength = strength  
        self.speed = speed
        self.texture = texture
        self.dead = False
        
        self.posX = posX
        self.posY = posY
        self.startX = posX
        self.startY = posY

        self.surface = pygame.image.load(texture).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (tileSize, tileSize))
        self.rect = self.surface.get_rect(topleft=(self.posX, self.posY))

    
    def draw(self, camera):
        screen.blit(self.surface, (self.posX - camera.offset_x, self.posY - camera.offset_y))

    def updatePosition(self, velX, velY):
        self.posX += velX
        self.posY += velY
        self.rect.topleft = (self.posX, self.posY)

        # Should also send a packet to the server
