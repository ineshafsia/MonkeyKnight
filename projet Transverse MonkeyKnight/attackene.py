def attack(typ,agr):
    if typ==1:
        cac()
    
    elif typ==2:
        spell()
        
    elif typ==3:
        spell()
        
    elif typ==4:
        #contact dmg
        pass
        
    elif typ==5:
        #contact dmg
        pass
    
    elif typ==6:
        cac()
        
    elif typ==7:
        if agr:
            #contact dmg
            pass
            
    elif typ==8:
        cac()
        #this one will boost the attack
        
    elif typ==9:
        spell()
        
    elif typ==10:
        cac()
        
    elif typ==11:
        #contact dmg ?
        pass

    elif typ==12:
        cac()
        #will attack all the case around him in aoe (upper half of a circle with him at the middle)
        
    elif typ==13:
        cac()
        #increase mvt speed
        
    elif typ==14:
        spell()
        
    elif typ==15:
        cac()
        
    elif typ==16:
        #shoot homing projectile
        pass
        
    elif typ==17:
        #implent strike here
        pass
    
    elif typ==19:
        cac()
        
        
#will need 4 type: touching, strike and homing
def spell(xs,ys,direction,image,rang,effect):
    if direction=="+":
        l=[]
        for i in range(rang):
            l.append([[xs[1]+i,ys[1]],image])
        return(l,effect)
    if direction=="-":
        l=[]
        for i in range(rang):
            l.append([[xs[0]-i,ys[1]],image])
        return(l,effect)        
def cac(xs,ys,direction,image,effect):
    if direction=="+":
        return([[[xs[1],ys[1]],image],[[xs[1]+1,ys[1]],image]],effect)
    if direction=="-":
        return([[[xs[0],ys[1]],image],[[xs[0]-1,ys[1]],image]],effect)