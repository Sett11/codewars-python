class Journey:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def isPossible(self):
        return self.c*4.8/1000 >= self.a['weight']+80*self.b


j = Journey({'weight': 45000}, 2, 9600000)

print(j.isPossible())
