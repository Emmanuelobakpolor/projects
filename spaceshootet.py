import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Space shooter")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)


spacex = 370
spacey = 410
changex = 0 


bulletx=386
bullety=415

score = 0


font = pygame.font.SysFont("Arial",30, "bold")


font_over = pygame.font.SysFont("Arial", 60, "bold")

alienpic=[]
alienspeedx = []
alienspeedy= []
alienx = []
alieny = []

no_of_aliens = 8

for i in range (no_of_aliens):
    alienx.append(random.randint(0, 734))
    alieny .append( random.randint(30,150))
    alienpic .append( pygame.image.load("alienboy.png"))
    alienspeedx.append(1.5)
    alienspeedy.append(40)





background= pygame.image.load("back.png")
playerimg = pygame.image.load("space-ship.png")
bulletpic = pygame.image.load("bullet.png")

check=False

running = True



def scoret():
    img=font.render(f"Score : {score}", True, "White")
    screen.blit(img, (10,10))


def gameover():
    imgover=font_over.render("GAMEOVER", True, "White")
    screen.blit(imgover,(250,250))



while running:
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_RIGHT:
                changex=-1
            if event.key == pygame.K_LEFT:
                changex = 1
            if event.key == pygame.K_SPACE:
                if check is False:
                    check = True
                    bulletx=spacex+16

        if event.type == pygame.KEYUP:
            changex=0
        
    spacex=spacex-changex
    if spacex<=0:
        spacex = 0
    elif spacex>=800-64:
        spacex=800-64



    for i in range (no_of_aliens):
        if alieny[i]>400:
            for j in range (no_of_aliens):
                alieny[j]=2000
            gameover()
            

        alienx[i]+=alienspeedx[i]
        if alienx[i]<=0:
            alienspeedx[i]=1
            alieny[i]+=alienspeedy[i]

        elif alienx[i]>=800-64:
            alienspeedx[i]=-1
            alieny[i]+=alienspeedy[i]

        distance = math.sqrt(math.pow(bulletx-alienx[i],2)+math.pow(bullety-alieny[i],2))
        if distance <25:           
            bullety=480
            check=False
            alienx[i]=random.randint(0, 734)
            alieny[i] = random.randint(30,150)
            score = score + 1
        screen.blit(alienpic[i], (alienx[i],alieny[i]))


    if bullety<=0:
        bullety=415
        check=False

    if check:
        screen.blit(bulletpic, (bulletx,bullety))
        bullety=bullety-3

    

    

    screen.blit(playerimg,(spacex,spacey))
    
    scoret()
    pygame.display.update()
