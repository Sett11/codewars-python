class SecureList:
    def __init__(self,items=[]):
        self.items=items[:]
        self.size=len(items)

    def __repr__(self):
        x=self.items
        self.items=str([])
        self.size=0
        return str(x)
    
    def __str__(self):
        x=self.items
        self.items=str([])
        self.size=0
        return str(x)
    
    def __getitem__(self,i):
        self.size-=1
        return self.items.pop(i)
    
    def __len__(self):
        return self.size

base=[1,2,3,4]
a=SecureList(base)

print(a[0],base[0])