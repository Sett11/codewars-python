class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
def dist(a,b):
    return (a.x-b.x)*(a.x-b.x)+(b.y-a.y)*(b.y-a.y)
    
def check(a,b,c,d):
    x,y,z=dist(a,b),dist(a,c),dist(a,d)
    if 0 in [x,y,z]:
        return False
    if (x==y and 2*x==z and 2*dist(b,d)==dist(b,c)) or\
    (y==z and 2*y==x and 2*dist(c,b)==dist(c,d)) or\
    (x==z and 2*x==y and 2*dist(b,c)==dist(b,d)):
        return True
    return False

def is_square(a):
    return check(*map(lambda x:Point(*x),a)) if len(a)==4 else False

print(is_square([(520, 520), (360, 521), (519, 360), (359, 361)]))