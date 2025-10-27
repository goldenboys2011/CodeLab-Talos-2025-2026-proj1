"""
Copyright: Odysseas Chryssos, Antonis Alexopoulos
All rights reserved 2025-2026
Cool Greek Games Studio
"""
import pygame 
import random
from classes.Camera import Camera
from classes.Weapon import Weapon
from classes.Defence import Defense
from classes.Entity import Entity
from classes.Tile import Tile
from config.config import screen, running, tileSize, clock, mapHeight, mapWidth

# === Setup ===
camera = Camera(400, 800)

# === Server Communication ===
def sendPacket(packetId):
    pass

# == Tile setup ==
grassFloor = []

for i in range(0, mapWidth):
    for j in range(0,mapHeight):
        if random.randint(0, 1) >= 0.2 : tile = "grass" 
        else: tile = "stone"
        grassFloor.append(Tile(tile, False, i * tileSize, j * tileSize))

# == Weapon Setup ==
knights_Sword = Weapon(90, "knights_Sword", "./media/grass.png")
knights_Shield = Defense(19)

# == Entity setup ===
knight = Entity(90, 10, 98, "knights_Sword","None", "knights_Shield", "./media/player.png")

# === Main Game loop ====
while running:
    dt = clock.tick(60) / 1000  # seconds since last frame (for frame-independent movement)
    pygame.display.flip()
    screen.fill("red")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    # === Key input ===
    keys = pygame.key.get_pressed()
    moveX, moveY = 0, 0
    speed = 200  # pixels per second

    if keys[pygame.K_a]:
        moveX -= 1
    if keys[pygame.K_d]:
        moveX += 1
    if keys[pygame.K_w]:
        moveY -= 1
    if keys[pygame.K_s]:
        moveY += 1

    # Normalize diagonal movement
    if moveX != 0 and moveY != 0:
        moveX *= 0.7071  # 1/sqrt(2)
        moveY *= 0.7071

    knight.updatePosition(moveX * speed * dt, moveY * speed * dt)           


    # === Object Drawing ===
    camera.follow(knight)

    for grass in grassFloor:
        grass.draw(camera)

    knight.draw(camera)