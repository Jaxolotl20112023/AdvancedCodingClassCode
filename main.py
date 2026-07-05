import pygame 
import time

pygame.init()

screenW = 700
screenH = 700

screen = pygame.display.set_mode( (screenW,screenH) )
screen.fill( (0,0,0) )

playerW = 100
playerH = 100 

playerX = 0
playerY = 0 

player = pygame.Rect(playerX,playerY,playerW,playerH) 

floorW = 700
floorH = 150 

floorX = 0
floorY = 550

floor = pygame.Rect(floorX,floorY,floorW,floorH)

blockW = 200
blockH = 150 

blockX = 300 
blockY = 400

block = pygame.Rect(blockX,blockY,blockW,blockH)

pygame.display.flip()

gravity = 5

running = True 
jump = False
clicked = False
while running == True : 

    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            running = False 

    if player.colliderect(floor) == False: 

        player.move_ip(0,gravity)

        if player.colliderect(block):
            player.move_ip(0,-gravity) 
            clicked = False

    else : 
        clicked = False

    if jump == True : 
        player.move_ip(0,-10)

    if player.y == playerY-200 : 
        jump = False

    if event.type == pygame.KEYDOWN : 

        if event.key == pygame.K_LEFT and (player.x)-30 >= 0:
        
            if not player.colliderect(block) and player.x < block.x + block.width : 
                player.move_ip(-10,0)

        if event.key == pygame.K_RIGHT and (player.x+player.width)+30 <= 700: 
            player.move_ip(10,0)

            if player.colliderect(block) and player.x+player.width > block.x: 
                player.move_ip(-10,0)

        if event.key == pygame.K_UP and clicked == False: 
            jump = True 
            clicked = True
            playerY = player.y
    

    # if event.type == pygame.KEYUP and clicked == True:
    #     clicked = False
        
        

    screen.fill( (0,0,0) )
    pygame.draw.rect(screen, (255,0,0), player)
    pygame.draw.rect(screen, (0,255,0), floor)
    pygame.draw.rect(screen, (0,0,255), block)
    pygame.display.update()

    time.sleep(0.01)
