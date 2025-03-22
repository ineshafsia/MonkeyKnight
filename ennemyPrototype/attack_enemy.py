from baseEnnemy import*

def attack(enemy,image,counter):
    typ = enemy.type
    if typ==1:
        if counter%240>=100 and counter%240<=140:
            if enemy.direction == "l":
                enemy.sprite = pygame.transform.scale(pygame.image.load("Ennemis\Scout\Scout_attaque.png"),(64,64))
            if enemy.direction == "r":
                enemy.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Ennemis\Scout\Scout_attaque.png"),(64,64)),True,False)
        if counter%240==120:
            return cac(enemy,image,None)
    
    elif typ==2:
        if counter%240>=100 and counter%240<=140:
            if enemy.direction == "l":
                enemy.sprite = pygame.transform.scale(pygame.image.load("Ennemis\Elfe\Elfe_attaque.png"),(64,64))
            if enemy.direction == "r":
                enemy.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Ennemis\Elfe\Elfe_attaque.png"),(64,64)),True,False)
        if counter%240==120:
            return spell(enemy,image,None)
        
    elif typ==3:
        if counter%240>=100 and counter%240<120:
            if enemy.direction == "l": 
                enemy.sprite = pygame.transform.scale(pygame.image.load("Ennemis\Chaman_ennemi\Chaman_ennemi_attaque1.png"),(64,64))
            if enemy.direction == "r":
                enemy.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Ennemis\Chaman_ennemi\Chaman_ennemi_attaque1.png"),(64,64)),True,False)
        elif counter%240>=120 and counter%240<=140:
            if enemy.direction == "l": 
                enemy.sprite = pygame.transform.scale(pygame.image.load("Ennemis\Chaman_ennemi\Chaman_ennemi_attaque2.png"),(64,64))
            if enemy.direction == "r":
                enemy.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Ennemis\Chaman_ennemi\Chaman_ennemi_attaque2.png"),(64,64)),True,False)
        if counter%240==120:
            spell(enemy,image,None)
        
    elif typ==4:
        return contact(enemy.x,enemy.y)
        
        
    elif typ==5:
        return contact(enemy.x,enemy.y)
    
    elif typ==6:
        if counter%120>=40 and counter%120<60:
            if enemy.direction == "l": 
                enemy.sprite = pygame.transform.scale(pygame.image.load("Ennemis\Mante\Mante_attaque1.png"),(64,64))
            if enemy.direction == "r":
                enemy.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Ennemis\Mante\Mante_attaque1.png"),(64,64)),True,False)
        elif counter%240>=120 and counter%240<=140:
            if enemy.direction == "l": 
                enemy.sprite = pygame.transform.scale(pygame.image.load("Ennemis\Mante\Mante_attaque2.png"),(64,64))
            if enemy.direction == "r":
                enemy.sprite = pygame.transform.flip(pygame.transform.scale(pygame.image.load("Ennemis\Mante\Mante_attaque2.png"),(64,64)),True,False)
        if counter%120==60:
            return cac(enemy,image,None)

        
def spell(enemy,image,effect):
    if enemy.direction=="r":
        enemy.list_projectile.append([[enemy.x,enemy.x+64],[enemy.y-64,enemy.y],image,effect])
    if enemy.direction=="l":
        enemy.list_projectile.append([[enemy.x-64,enemy.x],[enemy.y-64,enemy.y],image,effect])
            
def cac(enemy,image,effect):
    if enemy.direction=="r":
        return([enemy.x,enemy.x+128],[enemy.y-64,enemy.y],image)
    if enemy.direction=="l":
        return([enemy.x-128,enemy.x],[enemy.y-64,enemy.y])
    
def contact(xs,ys):
    return([xs,xs+64],[ys,ys+64])