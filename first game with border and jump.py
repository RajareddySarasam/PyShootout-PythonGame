import pygame
pygame.init()
window=pygame.display.set_mode((700,500))
pygame.display.set_caption("FIRST GAME")
clock=pygame.time.Clock()
run=True
isjump=False
jumpcount=10
x=350
y=250     
width=50
height=50
velocity=2
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
#MAIN LOOP
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>velocity:
        x-=velocity
    if keys[pygame.K_RIGHT]and x<700-width-velocity:
        x+=velocity
    if not(isjump):
        if keys[pygame.K_SPACE]:
            isjump=True
    else:
        if jumpcount>=-10:
            neg=1
            if jumpcount<0:
                neg=-1
            y-=(jumpcount**2)*0.2*neg
            jumpcount-=1
        else:
            isjump=False
            jumpcount=10
    window.blit(bg,(0,0))
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()
    clock.tick(60)
