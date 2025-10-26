"""
Copyright: Odysseas Chryssos, Antonis Alexopoulos
All rights reserved 2025-2026
Cool Greek Games Studio
"""
import pygame 
import random
import os

# === Setup ===
screen = pygame.display.set_mode((400,800))
pygame.display.toggle_fullscreen()
running = True

# === Variabled ===
tileSize = 50
tileTypeTextures = {
    "grass": "./media/grass.png",
    "stone": "./media/stone.png",
    "wood": "path",
    "wall": "path"
}

# === Classes ===
class Weapon():
    def __init__(self, streangth, name, texture):
        self.streangth = streangth
        self.name = name
        self.texture = texture
        
class Entity():
    def __init__(self, health, speed, strength, durabillity, weapon, secondary_weapon, shield, armor):
        self.strength = strength  
        self.durabillity = durabillity
        self.weapon = weapon
        self.secondary_weapon = secondary_weapon
        self.shield = shield
        self.armor = armor
        self.speed = speed
        self.health = health

    def attack(self, weapon, victim):
        if weapon == 1:
            weapon = self.weapon
        elif weapon == 2:
            weapon = self.secondary_weapon
        
         # Kai ean theloume prevent cheating k kala auto kanonika sto server (opos k genika to entity management)
        damageDealt = weapon.strength * (self.streangth / random.randint(0,1))
    
        victim.takeDamage(damageDealt) # Auto einai gia offline. gia online the prepi na stelnoume packet!
    
    def takeDamage(self, damageToBeDealt):
        self.health =- damageToBeDealt

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
            self.surface = pygame.transform.scale(self.surface, (50, 50))
        else:
            # fallback if missing
            self.surface = pygame.Surface((50, 50), pygame.SRCALPHA)
            self.surface.fill("blue")

        self.rect = self.surface.get_rect(topleft=(self.posX, self.posY))
    def draw(self):
        screen.blit(self.surface, self.rect)

# === Server Communication ===
def sendPacket(packetId):
    pass

# === Object Setup ===

# == Tile setup ==
grassFloor = []

for i in range(0, 40):
    for j in range(0,16):
        if random.randint(0, 1) >= 0.2 : tile = "grass" 
        else: tile = "stone"
        grassFloor.append(Tile(tile, False, i * 50, j * 50))

# == Entity setup ===
pass

# === Main Game loop ====
while running:
    pygame.display.flip()
    screen.fill("red")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    # === Object Drawing ===
    for grass in grassFloor:
        grass.draw()
