class Jar:
    def __init__(self):
        self.t=0
        self.store={}
    
    def add(self,amount,kind):
        if kind not in self.store:
            self.store[kind]=0
        self.store[kind]+=amount
        self.t+=amount
    
    def pour_out(self,amount):
        k=amount/self.t*100
        for i in self.store:
            self.store[i]-=self.store[i]/100*k
        self.t-=amount
    
    def get_total_amount(self):
        return self.t
    
    def get_concentration(self,kind):
        return self.store.get(kind,0)/self.t if self.t else 0

j=Jar()

j.add(200,'apple')
j.add(200,'orange')
j.pour_out(100)
print(j.get_concentration('apple'))