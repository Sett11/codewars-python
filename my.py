class IllegalArgumentError(BaseException):
    pass

class Graph:
    def __init__(self,v):
        if v<0:
            raise(IllegalArgumentError)
        self.v=v
        self.adj=[[] for _ in range(v)]
        self.uV=set()
        self.uE=set()
        self.V=v
        self.E=0

    def add_edge(self,v,w):
        if v<0 or w<0 or v>self.v or w>self.v:
            raise(IllegalArgumentError)
        if (v,w) not in self.uE and (w,v) not in self.uE:
            self.E+=1
            self.uE.add((v,w))
        self.adj[v].append(w)
        self.adj[w].append(v)
        if v not in self.uV:
            self.uV.add(v)
            if self.V<self.v:
                self.V+=1
        if w not in self.uV:
            self.uV.add(w)
            if self.V<self.v:
                self.V+=1

g=Graph(4)
g.add_edge(0, 1)
g.add_edge(2, 2)
print(g.V)
print(g.adj)