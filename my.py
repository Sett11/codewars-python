class Dinglemouse:
    def wrap(self,arg):
        if isinstance(arg,int):
            return f'I am {arg}.'
        if arg in 'MF':
            return f"I am {'male' if arg=='M' else 'female'}."
        return f'My name is {arg}.'

    def __init__(self):
        ...
    
    def setAge(self,age):
        self.age=age
        return self
        
    def setSex(self,sex):
        self.sex=sex
        return self
        
    def setName(self,name):
        self.name=name
        return self
        
    def hello(self):
        return ('Hello. '+' '.join(map(self.wrap,self.__dict__.values()))).strip()
    
dm = Dinglemouse().setName("Bob").setAge(27).setSex('M')
print(dm.hello())
dm.name='Jhon'
print(dm.hello())