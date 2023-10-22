class Person():
    def __init__(self,s):
        self.name=s
    def greet(self,c):
        return f'Hello {c}, my name is {self.name}'

g=Person('Joe')

print(g.greet('Kate'))
print(g.name)