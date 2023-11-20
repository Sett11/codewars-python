class Warrior:
    def __init__(self,name):
        self.name=name
        self.health=100
        
    def strike(self,enemy,swings):
        enemy.health-=swings*10
        if enemy.health<0:
            enemy.health=0