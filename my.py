def show_me(s):
    l,c=sorted(list(s.__dict__)),str(type(s)).split('.')[-1][:-2]
    return f"Hi, I'm one of those {c}s! Have a look at my {l[0]}." if len(l)==1 else f"Hi, I'm one of those {c}s! Have a look at my "+', '.join(l[:-1])+' and '+l[-1]+'.'

class Vehicle:
    def __init__(self, seats, wheels, engine):
        self.seats = seats
        self.wheels = wheels
        self.engine = engine

porsche = Vehicle(2, 4, 'gas')

print(show_me(porsche))