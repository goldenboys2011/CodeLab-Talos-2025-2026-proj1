import pygame 
import random

screen = pygame.display.set_mode((400,800))
pygame.display.toggle_fullscreen()
running = True

tileTypeTextures = {
    "grass": "path",
    "stone": "path",
    "wood": "path",
    "wall": "path"
}

class Weapon():
    def __init__(self, streangth, name, texture):
        self.streangth = streangth
        self.name = name
        self.texture = texture
        
class Entity():
    def __init__(self, speed, strength, durabillity, weapon, secondary_weapon, shield, armor ):
        self.strength = strength  
        self.durabillity = durabillity
        self.weapon = weapon
        self.secondary_weapon = secondary_weapon
        self.shield = shield
        self.armor = armor

    def attack(self, weapon, victim):
        if weapon == 1:
            weapon = self.weapon
        elif weapon == 2:
            weapon = self.secondary_weapon
    
        damageDealt = weapon.strength * (self.streangth / random.randint(0,1))
    
        victim.takeDamage(damageDealt)

class Tile():
    def init(self, typee, wall, positionX, positionY):

        self.passable = not wall
        self.texture = tileTypeTextures[typee]
        self.posX = positionX
        self.posY = positionY

        self.surface = pygame.Surface((20, 20), pygame.SRCALPHA)
        self.surface.fill("orange")

        self.rect = self.surface.get_rect(topleft=(self.posX, self.posY))
    def draw(self):
        screen.blit(self.surface, self.rect)

test = Tile("grass", False, 10, 10)

while running:
    pygame.display.flip()
    screen.fill("red")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.key.K_ESCAPE:
                pygame.quit()

    test.draw()
