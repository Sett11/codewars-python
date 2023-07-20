ROCKS={'Clay': (1, 5), 'Copper': (1, 17.5), 'Tin': (1, 17.5), 'Iron': (15, 35), 'Silver': (20, 40), 'Coal': (30, 50), 'Gold': (40, 65)}
EXPERIENCE={1: 0, 2: 83, 3: 174, 4: 276, 5: 388, 6: 512, 7: 650, 8: 801, 9: 969, 10: 1154, 11: 1358, 12: 1584, 13: 1833, 14: 2107, 15: 2411, 16: 2746, 17: 3115, 18: 3523, 19: 3973, 20: 4470, 21: 5018, 22: 5624, 23: 6291, 24: 7028, 25: 7842, 26: 8740, 27: 9730, 28: 10824, 29: 12031, 30: 13363, 31: 14833, 32: 16456, 33: 18247, 34: 20224, 35: 22406, 36: 24815, 37: 27473, 38: 30408, 39: 33648, 40: 37224}
class Miner:
    def __init__(self,x=0):
        self.x=x
        self.l=0
        for i in EXPERIENCE:
            if self.x>=EXPERIENCE[i] and i>self.l:
                self.l=i
    def mine(self,r):
        a=ROCKS[r]
        if a[0]>self.l:
            return f'You need a mining level of {a[0]} to mine {r}.'
        self.x+=a[1]
        for i in EXPERIENCE:
            if self.x>=EXPERIENCE[i] and i>self.l:
                self.l=i
                return f'Congratulations, you just advanced a Mining level! Your mining level is now {i}.'
        return 'You swing your pick at the rock.'

r=Miner()

print(r.mine('Tin'))
print(r.mine('Tin'))
print(r.mine('Tin'))
print(r.mine('Tin'))
print(r.mine('Tin'))
print(r.mine('Tin'))
print(r.mine('Tin'))
print(r.mine('Tin'))
print(r.mine('Iron'))