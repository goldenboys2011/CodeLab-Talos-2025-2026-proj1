import random
import pygame
from config.config import tileSize, screen

class Character():
    def __init__(self, health, speed, strength, weapon, secondary_weapon, shield, texture):
        self.strength = strength  
        self.weapon = weapon
        self.secondary_weapon = secondary_weapon
        self.shield = shield
        self.speed = speed
        self.health = health
        self.texture = texture

        self.dashing = False
        self.dash_dir = pygame.Vector2(0, 0)
        self.dash_time = 0
        self.dash_duration = 0.15  # seconds
        self.dash_speed = 800      # pixels per second

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

    def updatePosition(self, velX, velY, dt):
        # --- Handle dash movement ---
        if self.dashing:
            self.dash_time += dt
            if self.dash_time < self.dash_duration:
                self.posX += self.dash_dir.x * self.dash_speed * dt
                self.posY += self.dash_dir.y * self.dash_speed * dt
            else:
                self.dashing = False  # dash ended

        # --- Handle normal movement ---
        else:
            self.posX += velX * dt
            self.posY += velY * dt

        self.rect.topleft = (self.posX, self.posY)


