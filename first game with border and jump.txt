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
        if keys[pygame.K_UP]and y>velocity:
            y-=velocity
        if keys[pygame.K_DOWN]and y<500-height-velocity:
            y+=velocity
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
    window.fill("White")
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()
    clock.tick(60)
