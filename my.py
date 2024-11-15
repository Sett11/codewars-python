class Grid:
    def __init__(self,w,h):
        self.a=[['0']*w for _ in range(h)]
    def plot_point(self,x,y):
        self.a[y-1][x-1]='X'
        pass
    @property
    def grid(self):
        return '\n'.join(''.join(i) for i in self.a)

g=Grid(5,7)
g.plot_point(5,3)
print(g.grid)