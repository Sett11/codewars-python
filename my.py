class SimTime:
    def __init__(self):
        self.speed=1
        self.real_time=0
        self.time=0

    def get(self):
        return self.time
    
    def set_speed(self,n):
        self.speed=n

    def update(self,n):
        if n<self.real_time:
            raise()
        self.time+=(n-self.real_time)*self.speed
        self.real_time+=(n-self.real_time)

        
r=SimTime()

print(r.get())

r.update(10)
print(r.get())
r.update(12)
r.set_speed(3)
r.update(15)
print(r.get())
r.update(17)

print(r.get())