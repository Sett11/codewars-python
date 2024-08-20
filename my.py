glob_fack=[]

class Character:
    def __init__(self,name='Hero',strength=10,dexterity=10,intelligence=10):
        self.logs=[]
        self.events=[]
        self.prop={'limbs':[1,1,1,0]}
        self.shange=set()
        self.name=name
        self.strength=strength
        self.dexterity=dexterity
        self.intelligence=intelligence
        self.gang='limbs'
        self.gang_damage=self.strength+self.dexterity+self.intelligence

    def character_info(self):
        return f"{self.name}\nstr {self.strength}\ndex {self.dexterity}\nint {self.intelligence}\n{self.gang+('(enhanced)' if self.gang in self.shange else '')} {self.gang_damage} dmg"
        
    def event_log(self):
        return '\n'.join(self.logs)
    
    def f(self,a):
        return self.strength*a[0]+self.dexterity*a[1]+self.intelligence*a[2]+a[3]

    def add_gang(self,*args):
        t=glob_fack[-1]
        n=self.f(args)
        v=t in self.prop
        if v:
            self.shange.add(t)
            x=[max(i,j) for i,j in zip(self.prop[t],args)]
            y=self.f(x)
            if y>=self.gang_damage:
                r=sorted([t,self.gang])
                self.gang=r[0] if y==self.gang_damage else t
                self.gang_damage=y
            self.prop[t]=x
        elif n>self.gang_damage and not v:
            self.gang_damage=n
            self.gang=t
        elif n==self.gang_damage and not v:
            r=sorted([self.gang,t])
            self.gang=r[0]
        if not v:
            self.prop[t]=list(args)
        self.logs.append(f"{self.name} finds '{t}'")

    def change_properties(self,*args):
        t=glob_fack[-1]+': '
        if args[0]:
            self.strength+=args[0]
            t+=f'strength {"+" if args[0]>0 else ""}{args[0]}, '
        if args[1]:
            self.dexterity+=args[1]
            t+=f'dexterity {"+" if args[1]>0 else ""}{args[1]}, '
        if args[2]:
            self.intelligence+=args[2]
            t+=f'intelligence {"+" if args[2]>0 else ""}{args[2]}, '
        r,m=[],0
        for i in self.prop:
            x=self.f(self.prop[i])
            m=max(m,x)
            r.append((x,i))
        r=sorted([i for i in r if i[0]==m])
        if r:
            self.gang=r[0][1]
            self.gang_damage=self.f(self.prop[self.gang])
        else:
            self.gang_damage=self.f(self.prop[self.gang])
        self.logs.append(t.strip().strip(','))

    def __getattribute__(self,name):
        t=' '.join(name.split('_')).capitalize()
        try:
            atr=object.__getattribute__(self,name)
            glob_fack.append(t)
        except:
            if len(t.split())==3:
                object.__setattr__(self,name,self.add_gang)
                self.events.append(t)
                atr=object.__getattribute__(self,name)
            if len(t.split())==2:
                object.__setattr__(self,name,self.change_properties)
                atr=object.__getattribute__(self,name)
            glob_fack.append(t)
        return atr


ch = Character(name='Porky', strength=15, intelligence=7)
ch.pillar_of_water(4, 1, 2, 60)
ch.axe_of_fire(3, 1, 2, 20)
ch.dunder_of_water(0, 2, 0, 1)
ch.axe_of_fire(4, 0, 1, 60)
ch.staff_of_water(4, 1, 2, 60)

print(ch.character_info())