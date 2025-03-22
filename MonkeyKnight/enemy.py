from cmath import cos
import pygame
from attack import*

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)

'''
state = is the ennemy alive or dead
if state = true , the ennemy is alive
if state = false, the ennemy is dead
direction = the direction the ennemy is facing
l = the ennemy is facing left, r = the ennemy is facing right
type table:
1 = scout, 2 = elf, 3 = shaman
4 = big cockroach, 5 = bee, 6 = praying mantis
'''

class Ennemy:
    def __init__(self,x,y,dmg,hp,mv,type,aggression):
        data=ouverture("Data/dataenemy.txt")
        self.xs = pose[1]*64
        self.ys = pose[0]*64
        self.xs=[pose[1],pose[1]+1]
        self.ys=[pose[0],pose[0]+1]
        self.dmg = dmg
        self.hp = hp
        self.mv = mv
        self.type = type
        self.agression =  aggression
        self.state = True
        self.direction = '+'
        self.by = y
        self.imgimo=pygame.transform.scale(pygame.image.load(self.data[self.type][0]+"/A1.png"),(64,64))
        self.imgimoret=pygame.transform.flip(self.imgimo,True,False)
        self.img1=pygame.transform.scale(pygame.image.load(self.data[self.type][0]+"/A2.png"),(64,64))
        self.img1ret=pygame.transform.flip(self.img1,True,False)
        self.img2=pygame.transform.scale(pygame.image.load(self.data[self.type][0]+"/A3.png"),(64,64))
        self.img2ret=pygame.transform.flip(self.img2,True,False)
        self.img3=pygame.transform.scale(pygame.image.load(self.data[self.type][0]+"/A4.png"),(64,64))
        self.img3ret=pygame.transform.flip(self.img3,True,False)
        self.img4=pygame.transform.scale(pygame.image.load(self.data[self.type][0]+"/A5.png"),(64,64))
        self.img4ret=pygame.transform.flip(self.img3,True,False)
        
    def movement(self):
        if self.direction == '+':
            self.x += self.mv
        else:
            self.x-= self.mv
        if self.type ==  5:
            self. y = cos(self.count) + self.by
        
    
    def attack(self,typ):
        if typ==0:
            return coupbasique(self.xs,self.ys,self.direction,"Data/attaque/fistD.png",("None"),20)
        elif typ==2:
            return coupbasique(self.xs,self.ys,self.direction,"Data/attaque/slashTM.png",("First hit"),15)
        elif typ==3:
            return spell(self.xs,self.ys,self.direction,"Data/attaque/pic.png",5,("Slow"),10)
        elif typ==4:
            return spell(self.xs,self.ys,self.direction,"Data/attaque/fleche.png",7,["None"],10)
        elif typ==5:
            return spell(self.xs,self.ys,self.direction,"Data/attaque/Trait.png",5,["damage"],10)
        elif typ==6:
            return coupbasique(self.xs,self.ys,self.direction,"Data/attaque/slashTM.png","stun",10)
    
    def update(self):
        self.movement()
        #self.attack()
        
    def __str__(self):
        return "this unites deals {} damage, possesses {} health points and moves {} unites \nthe unit is at the position ({},{})".format(self.dmg,self.hp,self.mv,self.x,self.y)

def spell(xs,ys,direction,image,rang,effect,time):
    if direction=="+":
        l=[]
        for i in range(rang):
            l.append([[[xs[1]+i,ys[1]],image,direction]])
        return(l,effect,time)
    if direction=="-":
        l=[]
        for i in range(rang):
            l.append([[[xs[0]-i,ys[1]],image,direction]])
        return(l,effect,time)
    
def coupbasique(xs,ys,direction,image,effect,time):
    if direction=="+":
        return([[[[xs[1],ys[1]],image,direction]],[[[xs[1]+1,ys[1]],image,direction]]],effect,time)
    if direction=="-":
        return([[[[xs[0],ys[1]],image,direction]],[[[xs[0]-1,ys[1]],image,direction]]],effect,time)

def draw_window(ennemy):
    
    WIN.blit(ennemy.sprite,(ennemy.x,ennemy.y))
    

if __name__=="__main__":
    running = True
    counter = 0
    claude=Ennemy(0,0,10,10,1,3,True)
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        claude.update()
        draw_window(claude)
        counter+=1