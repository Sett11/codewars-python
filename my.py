class Menu:
    def __init__(self,a):
        self.a=a
        self.n=0

    def to_the_right(self):
        self.n+=1
        
    def to_the_left(self):
        self.n-=1
        
    def display(self):
        return str([[i] if j%len(self.a)==self.n%len(self.a) else i for j,i in enumerate(self.a)])

m=Menu([1, 2, 3])
m.to_the_right()
m.to_the_right()
m.to_the_right()
m.to_the_right()
m.to_the_left()
print(m.display())