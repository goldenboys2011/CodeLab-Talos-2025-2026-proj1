"""
Copyright: Odysseas Chryssos, Antonis Alexopoulos
All rights reserved 2025-2026
Cool Greek Games Studio
"""
import pygame 
from datetime import datetime, timedelta
from classes.Camera import Camera
from classes.Weapon import Weapon
from classes.Defence import Defense
from classes.Entities.Character import Character
from config.config import screen, running, clock
from classes.Entities.Projectiles.Arrow import Arrow
from screens.inGame import grassFloor, UI

# === Setup ===
camera = Camera(400, 800)
lastDash = datetime.now()

# === Server Communication ===
def sendPacket(packetId):
    pass

# == Weapon Setup ==
knights_Sword = Weapon(90, "knights_Sword", "./media/grass.png")
knights_Shield = Defense(19)

# == Entity setup ===
player = Character(90, 10, 98, knights_Sword,"None", "knights_Shield", "./media/player.png")
dummy = Character(90, 10, 98, knights_Sword,"None", "knights_Shield", "./media/player.png")
dummy.posX -= 250

testArrow = Arrow(600, 500, 5, 0, 5, 100, dummy)
arrows = [testArrow]

# === Main Game loop ====
while running:
    dt = clock.tick(60) / 1000
    pygame.display.flip()
    screen.fill("red")

    # === Key input ===
    keys = pygame.key.get_pressed()
    moveX, moveY = 0, 0
    speed = 200

    if keys[pygame.K_a]:
        moveX -= 1
        direction = "left"
    if keys[pygame.K_d]:
        moveX += 1
        direction = "right"
    if keys[pygame.K_w]:
        moveY -= 1
        direction = "up"
    if keys[pygame.K_s]:
        moveY += 1
        direction = "down"
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
            
        # DASH
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and datetime.now() - lastDash >= timedelta(seconds=0.5):
            lastDash = datetime.now()
            player.dashing = True
            player.dash_time = 0
            player.dash_dir = pygame.Vector2(0, 0)
            match direction:
                case "left":
                    player.dash_dir.x = -1
                case "right":
                    player.dash_dir.x = 1
                case "up":
                    player.dash_dir.y = -1
                case "down":
                    player.dash_dir.y = 1
        
    direction = "none"

    if moveX != 0 and moveY != 0:
        moveX *= 0.7071
        moveY *= 0.7071

    player.updatePosition(moveX * speed, moveY * speed, dt)

    # === Object Drawing ===
    for grass in grassFloor:
        grass.draw(camera)

    if not player.dead: 
        player.draw(camera) 
        camera.follow(player)
    else: camera.follow(player.killer)

    dummy.draw(camera)

    for arrow in arrows:
        arrow.update()
        arrow.draw(camera)

        if arrow.colideRect(player):
            arrow.dead = True
            player.takeDamage(arrow.strength, arrow.owner)
        if arrow.dead:
            arrows.remove(arrow)

    for item in UI:
        item.draw()