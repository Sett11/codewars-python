import networkx as nx

class Game():
    def __init__(self,a):
        self.a=a
        self.g=nx.Graph()
        n,m=len(a),len(a[0])
        for i in range(n):
            for j in range(m):
                if self.a[i][j]:
                    t=(i,j)
                    self.g.add_node(t)
                    for k in [(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0<=x<n and 0<=y<m and self.a[x][y]]:
                        self.g.add_edge(t,k)

    def play(self):
        return len(list(nx.algorithms.connected_components(self.g)))

g=Game([[1,0,1,0,1],
             [1,0,1,0,1],
             [1,1,1,0,0],
             [0,0,0,1,1],
             [0,0,0,1,1]])

print(g.play())