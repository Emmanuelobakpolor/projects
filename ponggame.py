import pygame
from pygame.locals import *


pygame.init()

screenwid = 700
screenhei = 600
white = (225,225,225)
cpu = 0
player = 0
font = pygame.font.SysFont("Consolas", 25, "bold")
speed = 5
changey = 0
fps = 60
margin = 50
winner = 0
liveball = False
speedinc = 1

fpsclock = pygame.time.Clock()
screen = pygame.display.set_mode((screenwid, screenhei))
pygame.display.set_caption("pong")



def board():
    screen.fill("black")
    pygame.draw.line(screen, white, (0,margin), (screenwid, margin))


def text_col():
    img = font.render(f"CPU : {cpu}", True,"White" )
    screen.blit(img,(10,10))

    img = font.render(f"PLAYER : {player}", True,"White" )
    screen.blit(img,(530,10))

    img = font.render(f"BALL SPEED : {speed}", True,"White" )
    screen.blit(img,(250, 10))
class paddle():
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.rect = Rect(self.x, self.y, 20, 100)
        self.speed = 5

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top>margin :
            self.rect.move_ip(0, -1 * self.speed)

        if key[pygame.K_DOWN]and self.rect.bottom<screenhei                                                                               :
            self.rect.move_ip(0, self.speed)

    def ai(self):
        if self.rect.centery <pong.rect.top and self.rect.bottom < screenhei:
            self.rect.move_ip(0, self.speed)
        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1 *self.speed)

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)


    

class ball():
    def __init__(self, x, y):
        self.reset(x,y)      
    
  

    def move(self):


        if self.rect.top < margin:
            self.speedy *= -1
        if self.rect.bottom > screenhei:
            self.speedy *= -1

        if self.rect.colliderect(playerpaddle)or self.rect.colliderect(cpupaddle):
            self.speedx*=-1
       

        if self.rect.left < 0:
            self.winner =1
        if self.rect.right > screenwid:
            self.winner = -1


        self.rect.x += self.speedx
        self.rect.y += self.speedy

        return self.winner

    def draw(self):
        pygame.draw.circle(screen, white, (self.rect.x + self.ballrad,self.rect.y + self.ballrad ),self.ballrad)

    def reset(self , x, y):
        self.x = x
        self.y = y
        self.ballrad = 8
        self.rect = Rect(self.x, self.y, self.ballrad*2, self.ballrad*2)
        self.speedx = -4
        self.speedy = 4
        self.winner =0
        

    
playerpaddle = paddle(screenwid-40, screenhei//2)
cpupaddle = paddle(20, screenhei//2)
pong = ball(screenwid -60, screenhei//2 + 60)



run = True
while run:
    fpsclock.tick(fps)
    board()
    text_col()

    playerpaddle.draw()
    cpupaddle.draw()
    playerpaddle.move()
   
    if liveball == True:
        speedinc+=1
        winner = pong.move()
        if winner == 0:
            playerpaddle.move()
            cpupaddle.ai()
            pong.draw()

        else:
            liveball = False
            if winner == 1:
                player +=1
            elif winner == -1:
                cpu += 1

    if liveball == False:
        if winner ==0:
            img = font.render("CLICK ANYWHERE TO START", True, "white", 200)
            screen.blit(img, (160,screenhei//2))
        
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and liveball == False:
            liveball = True
            pong.reset(screenwid -60, screenhei//2 + 60)

        if speedinc > 400:
            speedinc =0
            

    pygame.display.update()
pygame.quit()
