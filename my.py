from math import ceil

class Potion:
    def __init__(self, color, volume):
        self.color=color
        self.volume=volume
    
    def mix(self, other):
        r,n=[0]*3,self.volume+other.volume
        for i in range(3):
            r[i]=ceil((self.color[i]*self.volume+other.color[i]*other.volume)/n)
        return Potion(tuple(r),n)

potions = [
    Potion((153, 210, 199), 32),
    Potion((135,  34,   0), 17),
    Potion((18,   19,  20), 25),
    Potion((174, 211,  13),  4),
    Potion((255,  23, 148), 19),
    Potion((51,  102,  51),  6)
]
a = potions[0].mix(potions[1])
b = potions[0].mix(potions[2]).mix(potions[4])
c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])
d = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[4]).mix(potions[5])
e = potions[0].mix(potions[1]).mix(potions[2]).mix(potions[3]).mix(potions[4]).mix(potions[5])

print(e.color,e.volume)