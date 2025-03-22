# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:10:05 2022

@author: remir
"""

"""
0=Basique
1=Capusaint
2=Tue marin
3=albus Dumbabouin
4=Ouistitigre
5=Guenondorf
6=Guerille


1=size
"""
import pygame
def choice(Player,typ,xs,ys,direction):
    if typ==0:
        
        return coupbasique(xs,ys,direction,"Data/Attaque/FistD.png",("None"),20)
    
    elif typ==2:
        return coupbasique(xs,ys,direction,"Data/Attaque/slashTM.png",("First hit"),15)
    elif typ==3:
        return spell(xs,ys,direction,"Data/Attaque/pic.png",5,("Slow"),10)
    elif typ==4:
        return spell(xs,ys,direction,"Data/Attaque/Fleche.png",7,["None"],10)
    elif typ==5:
        return spell(xs,ys,direction,"Data/Attaque/Trait.png",5,["damage"],10)
    elif typ==6:
        return coupbasique(xs,ys,direction,"Data/Attaque/slashTM.png","stun",10)
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
def spell1(xs,ys,direction,image,rang,effect,time):
    if direction=="+":
        l=[]
        for i in range(rang):
            l.append([[[xs[1]+i,ys[1]-1],image,direction]])
        return(l,effect,time)
    if direction=="-":
        l=[]
        for i in range(rang):
            l.append([[[xs[0]-i,ys[1]-1],image,direction]])
        return(l,effect,time)    
def spellvert(xs,ys,direction,image,rang,effect,time):
    if direction=="+":
        l=[]
        j=[]
        for i in range(17):

            
            j.append([[xs[1],i],image,direction])
        
        l.append(j)
        return(l,effect,time)
    if direction=="-":
        l=[]
        j=[]
        for i in range(17):
            
            j.append([[xs[0]-1,i],image,direction])
        l.append(j)
        return(l,effect,time)       
def spellhorizon(xs,ys,direction,image,rang,effect,time):
    
        l=[]
        j=[]
        for i in range(21):

            
            j.append([[i,ys[1]],image,direction])
        
        l.append(j)
        return(l,effect,time)
    


            
   
def other(xs,ys,direction,image,effect,time):
    return([[[[xs[1],ys[1]],image,direction]]],effect,time)
    
def coupbasique(xs,ys,direction,image,effect,time):
    if direction=="+":
        return([[[[xs[1],ys[1]],image,direction]],[[[xs[1]+1,ys[1]],image,direction]]],effect,time)
    if direction=="-":
        return([[[[xs[0],ys[1]],image,direction]],[[[xs[0]-1,ys[1]],image,direction]]],effect,time)
def choice2(Player,typ,xs,ys,direction):
    if typ==0:
        
        return spell(xs,ys,direction,"attaque.png",7,["Size","Stun"],10)
    
    elif typ==2:
        return other(xs,ys,direction,"data/Attaque/cible.png",["other","*4","enemy"],5)
    elif typ==3:
        return spell(xs,ys,direction,"data/Attaque/ping.png",5,"*2 freeze",10)
    elif typ==4:
        return other(xs,ys,direction,"attaque.png",["other","Trap","immobile"],10)
    elif typ==5:
        return other(xs,ys,direction,"data/Attaque/cible.png",["other","copy","enemy"],5)
    elif typ==6:
        return coupbasique(xs,ys,direction,"Data/Attaque/slashTM.png",("armor","*2"),25)
def choice3(Player,typ,xs,ys,direction):
    if typ==0:
        
        return other(xs,ys,direction,"JeanEud.png",8,("damage","stun"),20)
    elif typ==1:
        return heal(Player,xs,ys,direction,"JeanEud.png","no damage")
    elif typ==2:
        return coupbasique(xs,ys,direction,"JeanEud.png","First hit")
    elif typ==3:
        return spell(xs,ys,direction,"attaque.png",5,None)
    elif typ==4:
        return spell(xs,ys,direction,"attaque.png",7,None)
    elif typ==5:
        return spell(xs,ys,direction,"attaque.png",1,"allydamage")
    elif typ==6:
        return coupbasique(xs,ys,direction,"JeanEud.png","stun")

def GearSimien(Player):
    Player.typ=8
    Player.img=Player.data[Player.type][0]
    Player.img=pygame.image.load(Player.data[Player.type][0]+".png")
    Player.img=pygame.transform.scale(Player.img, (64,64))
    Player.imgret=pygame.transform.flip(Player.img,True,False)
    Player.health=int(Player.data[Player.type][1])
    Player.attack=int(Player.data[Player.type][3])
def heal(Player,xs,ys,direction,image,effect):
    if Player.hp+10<=Player.basehealth:
       Player.hp=Player.basehealth 
    else:
        Player.vie+=10
    return([[xs[0],ys[1]],image],effect)
    