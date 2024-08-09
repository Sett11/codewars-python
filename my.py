class Router:
    def __init__(self):
        self.db={}
    
    def bind(self,a,b,c):
        self.db[(a,b)]=c
    
    def runRequest(self,a,b):
        try:
            return self.db[(a,b)]()
        except KeyError:
            return 'Error 404: Not Found'