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
pML = False
pMR = False
pMU = False
pMD = False
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

class Defense():
    def __init__(self, durabillity):
        self.Durabillity = durabillity #Counted in how many hits it takes before it breaks
        


        
class Entity():
    def __init__(self, health, speed, strength, weapon, secondary_weapon, shield, texture):
        self.strength = strength  
        self.weapon = weapon
        self.secondary_weapon = secondary_weapon
        self.shield = shield
        self.speed = speed
        self.health = health
        self.texture = texture

        self.posX = 50
        self.posY = 50

        self.surface = pygame.image.load(texture).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (50, 50))
        self.rect = self.surface.get_rect(topleft=(self.posX, self.posY))
        
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
    
    def draw(self):
        screen.blit(self.surface, self.rect)

    def updatePosition(self, velX, velY):
        self.posX += velX
        self.posY += velY
        self.surface = pygame.transform.scale(self.surface, (50, 50))
        self.rect = self.surface.get_rect(topleft=(self.posX, self.posY))

        # Should also send a packet to the server




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


                  #==Weapons/Gear==
knights_Sword = Weapon(90, "knights_Sword", "./media/grass.png")
knights_Shield = Defense(19)

                        #==Characters==

knight = Entity(90, 1, 98, "knights_Sword","None", "knights_Shield", "./media/player.png")

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

            # === Movement ===
            if event.key == pygame.K_a:
                pML = True
                pMR = False
                
            if event.key == pygame.K_d:
                pMR = True
                pML = False
            
            if event.key == pygame.K_w:
                pMU = True
                pMD = False
            
            if event.key == pygame.K_s:
                pMD = True
                pMU = False
                                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                pML = False
                
            if event.key == pygame.K_d:
                pMR = False  
            
            if event.key == pygame.K_w:
                pMU = False  

            if event.key == pygame.K_s:
                pMD = False  
        

        if pMD:
            knight.updatePosition(0, (1.2 * knight.speed))
        elif pMU:
            knight.updatePosition(0, -(1.2 * knight.speed))
        if pMR:
            knight.updatePosition((1.2 * knight.speed), 0)
        if pML:
            knight.updatePosition(-(1.2 * knight.speed), 0)


    # === Object Drawing ===
    for grass in grassFloor:
        grass.draw()

    knight.draw()