import pygame
import levelWithEnemy
from typing import List

screen =pygame.display.set_mode((1280,704))
continu=1 
save=levelWithEnemy.ouverture("save.txt")[0]
lev=0   
niveau=0
niv=[]
time=0
screen_width: int = 1280
screen_height: int = 704
menu1: pygame.Surface = pygame.transform.scale(
     pygame.image.load("Data/main1.png"), (screen_width, screen_height))
menu2: pygame.Surface=pygame.transform.scale(
     pygame.image.load("Data/main2.png"), (screen_width, screen_height))
image3: pygame.Surface=pygame.transform.scale(
     pygame.image.load("Data/gameover.png"), (screen_width, screen_height))

clock: pygame.time.Clock = pygame.time.Clock() 
clock.tick(60)
ally: List=[]
play: int=0
pos: List[int]=[0,0]

while continu>0:
    for event in pygame.event.get():
        if niveau==0:
            if time<15:
                screen.blit(menu1,(0,0))
            else:
                screen.blit(menu2,(0,0))
            
            pygame.display.flip()
            if time==30:
                time=0
            time+=1

        if play==2:
                screen.blit(image3,(0,0))
                pygame.display.flip()
        if event.type == pygame.QUIT:
            continu=0

        if event.type== pygame.MOUSEBUTTONUP:
            pos: int = pygame.mouse.get_pos()

        if play==0:
            if pos[0]>406 and pos[0]<581:
                if pos[1]>517 and pos[1]<593:
                    play=1
            if pos[0]>664 and pos[0]<869:
                if pos[1]>521 and pos[1]<592:
                    continu=0

        if play==2:
            if pos[0]>450 and pos[0]<830:
                if pos[1]>516 and pos[0]<582:
                    save=levelWithEnemy.ouverture("save.txt")[0]
                    lev: int=0   
                    niveau: int=0
                    niv: List=[]
                    time: int=0
                    ally: List=[]
                    play: int=0

        if play==1:
            if niveau==0:
                    delta=levelWithEnemy.main("Chooselevel.txt",[],screen,ally)
                    niveau+=1

            if niveau>0:
                (continu,lastlevel)=levelWithEnemy.main(save[lev][0],niv,screen,ally)
                
                if lastlevel==0:
                        play=2
                else:
                    niv.append(lastlevel)
                    niveau+=1