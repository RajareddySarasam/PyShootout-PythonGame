import pygame
pygame.init()
window=pygame.display.set_mode((700,480))
pygame.display.set_caption("FIRST GAME")
clock=pygame.time.Clock()
walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkleft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
class player:
    def __init__(self,x,y,width,height,velocity):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velocity=velocity
        self.walkcount=0
        self.isjump=False
        self.left=False
        self.right=False
        self.jumpcount=10
    def draw(self,window):
        if self.walkcount+1>=30:
            self.walkcount=0
        if self.left:
            window.blit(walkleft[self.walkcount//7],(self.x,self.y))
            self.walkcount+=1
        elif self.right:
            window.blit(walkright[self.walkcount//7],(self.x,self.y))
            hero.walkcount+=1
        else:
            window.blit(char,(self.x,self.y))
        pygame.display.update()
def redrawgamewindow():
    window.blit(bg,(0,0))
    hero.draw(window)
    pygame.display.update()
    
#MAIN LOOP
hero=player(100,410,50,50,3)
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hero.x>hero.velocity:
        hero.x-=hero.velocity
        hero.left=True
        hero.right=False
    elif keys[pygame.K_RIGHT]and hero.x<700-hero.width-hero.velocity:
        hero.x+=hero.velocity
        hero.left=False
        hero.right=True
    else:
        hero.left=False
        hero.right=False
        hero.walkcount=0
    if not(hero.isjump):
        if keys[pygame.K_SPACE]:
            hero.isjump=True
            hero.right=False
            hero.left=False
            hero.walkcount=0
    else:
        if hero.jumpcount>=-10:
            neg=1
            if hero.jumpcount<0:
                neg=-1
            hero.y-=(hero.jumpcount**2)*0.2*neg
            hero.jumpcount-=1
        else:
            hero.isjump=False
            hero.jumpcount=10
    redrawgamewindow()
    pygame.display.update()
    clock.tick(30)
