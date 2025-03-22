from multiprocessing import Condition
import pygame

class BobLeGlorieux:
    ##BEHOLD THE GLORIOUS BEHING Bob, THE MOST GLORIOUS MONSTER TO EVER EXIST
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dmg = 10**25
        self.mv = 0.03
        self.state = True
        self.sprite_base = "Ennemis\Bob\Bob"
        self.sprite = pygame.image.load(self.sprite_base+"1.png")
        
    def gloriousCharge(self,counter):
        if counter%360<180:
            self.sprite = pygame.image.load(self.sprite_base+"1.png")
        elif counter%360>=180:
            self.sprite = pygame.image.load(self.sprite_base+"2.png")
        self.x-= round(self.mv,2)
        
    def contact(xs,ys):
        return([xs,xs+64],[ys,ys+64])
        
class Design_original:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dmg = 15
        self.mv = 0.3
        self.state = True
        self.direction = 'r'
        self.sprite_base = "Ennemis\DESIGN_ORIGINAL.PNG\DESIGN_ORIGINAL"
        self.sprite = pygame.transform.scale(pygame.image.load(self.sprite_base+"1.png"),(64,64))
        
    def change2Sprite(self,counter,total_counter,transition_point):
        if self.direction == "r":
            if counter%total_counter<transition_point:
                self.sprite = pygame.transform.scale(pygame.image.load(self.sprite_base+"1.png"),(64,64))
            elif counter%total_counter>=transition_point:
                self.sprite = pygame.transform.scale(pygame.image.load(self.sprite_base+"2.png"),(64,64))
        elif self.direction == "l":
            if counter%total_counter<transition_point:
                self.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.sprite_base+"1.png"),(64,64)),True,False)
            elif counter%total_counter>=transition_point:
                self.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load(self.sprite_base+"2.png"),(64,64)),True,False)  
            
    def detectionWalls(self,low_x,high_x):
        if self.x-self.mv <= low_x:
            self.direction = 'r'
        elif self.x+self.mv+64 >= high_x:
            self.direction = 'l'
        
    def wakuwaku(self,counter):
        self.detectionWalls(0,1280)
        self.change2Sprite(counter,240,120)
        if self.direction == 'r':
            self.x +=round(self.mv,2)
        else:
            self.x-= round(self.mv,2)
            
def contact(xs,ys):
    return [xs[1],ys[1]]

def movementBoss(Boss):
    if Boss.direction == 'r':
        Boss.x+=Boss.mv
    else:
        Boss.x-=Boss.mv
        
class Bouton:
    def __init__(self,x,y):
        self.lx = x
        self.hy = y
        self.rx = x+64
        self.ly = y-64
        self.visibility = False
        self.activation_state = False
        self.sprite = None
        
def showButton(Bouton,counter):
    if Bouton.visiblity == True:
        if Bouton.activation_state == False:
            Bouton.sprite =pygame.transform.scale(pygame.image.load("button1.png"),(64,64))
        elif Bouton.activation_state == True:
            Bouton.sprite =pygame.transform.scale(pygame.image.load("button2.png"),(64,64)) 
        
def buttonActivation(Bouton,px,py,counter):
    if Bouton.activation_state == False and Bouton.visiblity == True:
        condition_x = False
        for i in range(2):
            if px[i]>=Bouton.lx and px[i]<=Bouton.rx:
                condition_x = True
        if condition_x:
            condition_y = False
            for i in range(2):
                if py[i]>=Bouton.ly and px[i]<=Bouton.hy:
                    condition_y = True
            if condition_y:
                Bouton.activation_state = True

def defeatBoss(design_original, br):
    if br == 1:
        design_original.mv+=0.1
        design_original.sprite_base = "Ennemis\DESIGN_ORIGINAL.PNG\DESIGN_ORIGINAL_angry"
    if br == 0:
        design_original.state = False
        print("margaret tatcher is dead, ding dong the wicked bitch is dead")
    else:
        print("JOE BAMA ")
        
def countRemainingButon(list_buton):
    return len(list_buton)

def deleteButon(list_buton):
    return list_buton[1:]

if __name__=='__main__':
    Ines = Bouton(0,0)
    margaret_tatcher = Design_original(0,0)
    L_buton=[]
    for i in range(3):
        L_buton.append(Bouton(i,i))
    buton_remaining = countRemainingButon(L_buton)
    for i in range(buton_remaining):
        L_buton = deleteButon(L_buton)
        buton_remaining = countRemainingButon(L_buton)
        defeatBoss(margaret_tatcher,buton_remaining)
        