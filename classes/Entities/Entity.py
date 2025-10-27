import random
import pygame
from config.config import tileSize, screen

class Entity():
    def __init__(self, health, speed, strength, weapon, secondary_weapon, shield, texture):
        self.strength = strength  
        self.weapon = weapon
        self.secondary_weapon = secondary_weapon
        self.shield = shield
        self.speed = speed
        self.health = health
        self.texture = texture

        self.posX = 800
        self.posY = 500

        self.surface = pygame.image.load(texture).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (tileSize, tileSize))
        self.rect = self.surface.get_rect(topleft=(self.posX, self.posY))
        
    def attack(self, weapon, victim):
        if weapon == 1:
            weapon = self.weapon
        elif weapon == 2:
            weapon = self.secondary_weapon
        
         # Kai ean theloume prevent cheating k kala auto kanonika sto server (opos k genika to entity management)
        damageDealt = weapon.strength * (self.streangth / random.uniform(0.5, 1.5))
    
        victim.takeDamage(damageDealt) # Auto einai gia offline. gia online the prepi na stelnoume packet!
    
    def takeDamage(self, damageToBeDealt):
        self.health -= damageToBeDealt
    
    def draw(self, camera):
        screen.blit(self.surface, (self.posX - camera.offset_x, self.posY - camera.offset_y))

    def updatePosition(self, velX, velY):
        self.posX += velX
        self.posY += velY
        self.rect.topleft = (self.posX, self.posY)

        # Should also send a packet to the server
