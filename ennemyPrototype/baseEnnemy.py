from math import*
from random import randint
import pygame
from attack_enemy import*
from boss_miniboss import*


NUMBER_ENEMY = 18

'''
what is missing :
update elfe and chamans projectiles

'''


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

class Enemy:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.dmg = None
        self.hp = None
        self.mv = None
        self.type = type
        self.agression =  None
        self.state = True
        self.direction = 'l'
        self.by = y
        self.sprite = None
        self.stats = None
        self.sprite_attack = None
        self.nb_attck_frame = None
        self.TOD = None
        
    def change3Sprite(self,counter,total_counter,transition_point_1,transition_point_2):
        if self.direction == 'l':
            if counter%total_counter<transition_point_1: 
                self.sprite = pygame.transform.scale(pygame.image.load(self.stats[0]+"1.png"),(64,64))
            elif counter%total_counter>=transition_point_1 and counter%total_counter<transition_point_2:
                self.sprite = pygame.transform.scale(pygame.image.load(self.stats[0]+"2.png"),(64,64))
            elif counter%total_counter>=transition_point_2:
                self.sprite = pygame.transform.scale(pygame.image.load(self.stats[0]+"3.png"),(64,64))
        elif self.direction == 'r':
            if counter%total_counter<transition_point_1: 
                self.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.stats[0]+"1.png"),(64,64)),True,False)
            elif counter%total_counter>=transition_point_1 and counter%total_counter<transition_point_2:
                self.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.stats[0]+"2.png"),(64,64)),True,False)
            elif counter%total_counter>=transition_point_2:
                self.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.stats[0]+"3.png"),(64,64)),True,False)
    
    def change2Sprite(self,counter,total_counter,transition_point):
        if self.direction == "l":
            if counter%total_counter<transition_point:
                self.sprite = pygame.transform.scale(pygame.image.load(self.stats[0]+"1.png"),(64,64))
            elif counter%total_counter>=transition_point:
                self.sprite = pygame.transform.scale(pygame.image.load(self.stats[0]+"2.png"),(64,64))
        elif self.direction == "r":
            if counter%total_counter<transition_point:
                self.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.stats[0]+"1.png"),(64,64)),True,False)
            elif counter%total_counter>=transition_point:
                self.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.stats[0]+"2.png"),(64,64)),True,False)  
                            
    def detectionWalls(self,low_x,high_x):
        if self.x-self.mv <= low_x:
            self.direction = 'r'
        elif self.x+self.mv+64 >= high_x:
            self.direction = 'l'
        
    def movement(self,counter):
        self.detectionWalls(0,1280)
        if self.type!=3:
            if self.type == 6:
                self.change3Sprite(counter,60,20,40)
            elif self.type == 5: #60 30
                self.change2Sprite(counter,60,30)
                self. y = round(75*cos(counter/(self.mv*275)) + self.by,2)
            else :
                self.change2Sprite(counter,240,120)
            if self.direction == 'r':
                self.x +=round(self.mv,2)
            else:
                self.x-= round(self.mv,2)
        
    def get_TOD(self,counter):
        if self.type == 4 and self.state == False:
            self.TOD = counter
        
    def revive(self,counter):
        if self.type == 4 and self.TOD != None:
            if counter == self.TOD+60*5:
                self.state == True
                self.TOD = None
            else:
                if self.state == False:
                    if counter%120<60:
                        self.sprite = pygame.transform.scale(pygame.image.load(self.stats[0]+"_mort_1.png"),(64,64))
                    elif counter%120>=60:
                        self.sprite = pygame.transform.scale(pygame.image.load(self.stats[0]+"_mort_2.png"),(64,64))
                        
    def block(self):
        if self.type == 6:
            if randint(1,3)==3:
                return 0
        return 1

    def __str__(self):
        return "this unites deals {} damage, possesses {} health points and moves {} unites \nthe unit is at the position ({},{})".format(self.dmg,self.hp,self.mv,self.x,self.y)
    

def recupStatsEnemy(enemy,type):
    with open("Enemy_stats.txt",'r',encoding="utf-8") as f:
        temp_lines = f.readlines()
    line = temp_lines[type-1].strip("\n")
    stats = line.split(" ")
    enemy.stats = stats
    enemy.dmg = float(stats[1])
    enemy.hp = float(stats[2])
    enemy.mv = float(stats[3])
    enemy.agression = bool(stats[4])
    enemy.sprite = pygame.transform.scale(pygame.image.load(stats[0]+"1.png"),(64,64))
    enemy.nb_attack_frame = int(stats[5])
    enemy.list_projectile = []
    if enemy.nb_attack_frame == 1:
        enemy.sprite_attack = pygame.transform.scale(pygame.image.load(stats[0]+"_attaque.png"),(64,64))
    elif enemy.nb_attack_frame > 1:
        enemy.sprite_attack = pygame.transform.scale(pygame.image.load(stats[0]+"_attaque1.png"),(64,64))

           
if __name__=="__main__":
    running = True
    counter = 0
    L_enemies = []
    for i in  range (6):
        L_enemies.append(Enemy(1200,i*100,i+1))
        recupStatsEnemy(L_enemies[i],L_enemies[i].type)
    L_enemies.append(BobLeGlorieux(1200,600))
    L_enemies.append(Design_original(1200,700))
    
    L_buton=[]
    for i in range(3):
        L_buton.append(Bouton(i,i))
    buton_remaining = countRemainingButon(L_buton)
    pygame.init()
    
    #### Create a canvas on which to display everything ####
    window = (1280,780)
    screen = pygame.display.set_mode(window)
    #### Create a canvas on which to display everything ####

    #### Create a surface with the same size as the window ####
    background = pygame.Surface(window)
    
    
    #### Blit the surface onto the canvas ###
    screen.blit(background,(0,0))
    for i in range(len(L_enemies)):
        screen.blit(L_enemies[i].sprite,(L_enemies[i].x,L_enemies[i].y))
    
    #### Update the the display and wait ####
    
    
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(30)
    
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        counter+=1
        
        
        if counter == 1200:
            L_buton = deleteButon(L_buton)
            L_buton = deleteButon(L_buton)
            buton_remaining = countRemainingButon(L_buton)
            defeatBoss(L_enemies[-1],buton_remaining)
        screen.blit(background,(0,0))
        
        
        for i in range(len(L_enemies)):
            if i<6:
                L_enemies[i].movement(counter)
                attack(L_enemies[i],1,counter)
                screen.blit(L_enemies[i].sprite,(L_enemies[i].x,L_enemies[i].y))
            elif i == 6:
                L_enemies[i].gloriousCharge(counter)
                screen.blit(L_enemies[i].sprite,(L_enemies[i].x,L_enemies[i].y))
            else:
                L_enemies[i].wakuwaku(counter)
                screen.blit(L_enemies[i].sprite,(L_enemies[i].x,L_enemies[i].y))
        pygame.display.flip()
    #### Update the the display and wait ####

    pygame.quit()