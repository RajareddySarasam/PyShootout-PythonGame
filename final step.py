import pygame
pygame.init()
window=pygame.display.set_mode((700,480))
pygame.display.set_caption("FIRST GAME")
clock=pygame.time.Clock()
score=0
walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkleft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
bulletsound=pygame.mixer.Sound('bullet.mp3')
hitsound=pygame.mixer.Sound('hit.mp3')

bgmusic=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
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
        self.hitbox=(self.x+15,self.y+15.5,38,50)

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
            if self.right:
                window.blit(walkright[0],(self.x,self.y))
            elif self.left:
                window.blit(walkleft[0],(self.x,self.y))
            else:
                window.blit(char,(self.x,self.y))
        self.hitbox=(self.x+15,self.y+15.5,38,50)
        #pygame.draw.rect(window,"Green",self.hitbox,1)
        pygame.display.update()

    def hit(self):
        self.isjump=False
        self.jumpcount=10
        self.x=100
        self.y=410
        self.walkcount=0
        font1=pygame.font.SysFont('comicsans',50,True)
        text=font1.render('-5',1,"Red")
        window.blit(text,(314-(text.get_width()/4),105))
        pygame.display.update()
        i=0
        while i<300:
            pygame.time.delay(12)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()
                    break         


class enemy:
    walkright = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),pygame.image.load("R10E.png"),pygame.image.load("R11E.png")]
    walkleft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),pygame.image.load("L10E.png"),pygame.image.load("L11E.png")]
    def __init__(self,x,y,width,height,end,velocity):
        self.x= x
        self.y= y
        self.width=width
        self.height=height
        self.end=end
        self.walkcount=0
        self.velocity=velocity
        self.path=[self.x,self.end]
        self.hitbox=(self.x+20,self.y+10,30,40)
        self.health=10
        self.visible=True
    def draw(self,window):
        if self.visible:
            self.move()
            if self.walkcount+1>33:
                self.walkcount=0
            if self.velocity>0 :
                window.blit(self.walkright[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            else:
                window.blit(self.walkleft[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            self.hitbox=(self.x+20,self.y+10,30,50)
            #pygame.draw.rect(window,"Red",self.hitbox,1)
            pygame.draw.rect(window,"Red",(self.x,self.y-20,50,10))
            pygame.draw.rect(window,(0,123,0),(self.x,self.y-20,50-(5*(10-self.health)),10))
    def move(self):
        if self.velocity >0:
            if self.x+self.velocity < self.end:
                self.x+=self.velocity
            else:
                self.velocity=self.velocity*-1
                self.walkcount=0
        else:
            if self.x-self.velocity>self.path[0]:
                self.x+=self.velocity
            else:
                self.velocity=self.velocity*-1
                self.walkcount=0
    def hit(self):
        if self.health>1:
            self.health-=1
        else:
            self.visible=False
class projectile:
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=3*self.facing
    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)
        
def redrawgamewindow():
    window.blit(bg,(0,0))
    text=font.render('Score:'+ str(score),1,"Orange")
    window.blit(text,(570,10))
    vilan.draw(window)
    hero.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()
    
#MAIN LOOP
hero=player(100,410,50,50,3)
vilan=enemy(150,410,50,50,400,3)
font=pygame.font.SysFont("comicsans",30,True)
shootloop=0
bullets=[]
run=True
while run:
    if vilan.visible:
        if hero.hitbox[1]< vilan.hitbox[3]+vilan.hitbox[1] and hero.hitbox[1]+hero.hitbox[3]>vilan.hitbox[1]:
            if hero.hitbox[0]+hero.hitbox[2]>vilan.hitbox[0] and hero.hitbox[0]<vilan.hitbox[0]+vilan.hitbox[2]:
                hero.hit()
                score-=5
    if shootloop>0:
        shootloop+=1
    if shootloop==10:
        shootloop=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break

    if hero.left:
        facing=-1
    else:
        facing=1
    for bullet in bullets:
        
        if bullet.y-bullet.radius> vilan.hitbox[1] and bullet.y+bullet.radius<vilan.hitbox[1]+vilan.hitbox[3]:
            if bullet.x-bullet.radius>vilan.hitbox[0] and bullet.x+bullet.radius<vilan.hitbox[0]+vilan.hitbox[2]:
                hitsound.play()
                vilan.hit()
                score+=1
                bullets.pop(bullets.index(bullet))
    
        if bullet.x<698 and bullet.x>2:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop==0:
        bulletsound.play()
        if len(bullets)<7:
            bullets.append(projectile(round(hero.x+hero.width//2),round(hero.y+hero.height//2),4,"Red",facing))
            shootloop=1

    if keys[pygame.K_LEFT] and hero.x>hero.velocity:     
        hero.x-=hero.velocity
        hero.left=True
        hero.right=False
    elif keys[pygame.K_RIGHT]and hero.x<700-hero.width-hero.velocity:
        hero.x+=hero.velocity
        hero.left=False
        hero.right=True
    else:
        hero.walkcount=0

    if not(hero.isjump):
        if keys[pygame.K_UP]:
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
