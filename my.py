class Vector:
    def __init__(self,*a):
        if len(a)==1:
            a=a[0]
        self.x,self.y,self.z=a
        self.magnitude=(self.x**2+self.y**2+self.z**2)**.5

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
    
    def __eq__(self,other):
        return isinstance(other,Vector) and [self.x,self.y,self.z]==[other.x,other.y,other.z]
    
    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'
    
    def to_tuple(self):
        return self.x,self.y,self.z
    
    def cross(self,other):
        return Vector(self.y*other.z-self.z*other.y,self.z*other.x-self.x*other.z,self.x*other.y-self.y*other.x)

    def dot(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    

v=Vector(1,2,3)
print(v.cross(Vector([4,5,6])))