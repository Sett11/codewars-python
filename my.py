from preloaded import ACTIONS

class Machine:
    def __init__(self):
        self.c=0
        self.act=[0]*5
    
    def command(self,cmd,num):
        self.c=cmd
        return ACTIONS()[self.act[self.c%5]%5](num)
        
    def response(self,res):
        if not res:
            self.act[self.c%5]+=1