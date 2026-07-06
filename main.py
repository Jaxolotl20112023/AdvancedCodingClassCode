import pygame 
import time

pygame.init()

def collision(shape1,shape2) :

    if (shape1.x < shape2.x + shape2.width and shape1.x + shape1.width > shape2.x and shape1.y < shape2.y+shape2.height and shape1.y+shape1.height > shape2.y) :
        print("Collide!")
        return True
    
    return False

class Player() : 

    def __init__(self,x,y,width,height) : 
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.xV = 0
        self.yV = 0
        self.grounded = False 

        self.player = pygame.Rect(x,y,width,height)   

    def draw(self) : 
        pygame.draw.rect(screen, (255,0,0), self.player)

    def input(self) : 
        self.xV = 0 
        if event.type == pygame.KEYDOWN : 

            if event.key == pygame.K_LEFT:
                self.xV = -15

            if event.key == pygame.K_RIGHT: 
                self.xV = 15

            if event.key == pygame.K_UP and self.grounded: 
                self.grounded = False 
                self.yV = -30

    def movement_collision(self) : 
        self.yV += gravity

        self.player.x += self.xV

        for shape in platforms :
            if self.player.colliderect(shape) : 
                print("collide")
                if self.xV < 0: 
                    self.player.left = shape.right
                elif self.xV > 0:
                    self.player.right = shape.left

        self.player.y += self.yV
        self.grounded = False

        for shape in platforms : 
            if self.player.colliderect(shape) : 
                if self.yV > 0: 
                    self.player.bottom = shape.top
                    self.yV = 0 
                    self.grounded = True

                elif self.yV < 0:
                    self.player.top = shape.bottom  
                    self.yV = 0


# make screen
screenW = 700
screenH = 700

screen = pygame.display.set_mode( (screenW,screenH) )
screen.fill( (0,0,0) )

# make shapes
player = Player(0,0,50,50)

platforms  = [
    pygame.Rect(0,550,700,150),
    pygame.Rect(300,400,200,150),
    pygame.Rect(0,450,200,150)
]

pygame.display.flip()

gravity = 1
playerXVel = 0
playerYVel = 0

running = True 
grounded = False
clicked = False
while running == True : 

    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            running = False

    # collision(player,block)
    player.input()
    

    player.movement_collision()

    screen.fill( (0,0,0) )
    player.draw()

    for shape in platforms: 
        pygame.draw.rect(screen, (0,255,0), shape)
    
    
    pygame.display.update()

    time.sleep(0.01)
