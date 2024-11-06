from sys import setrecursionlimit
setrecursionlimit(10000)

class Graph:
    def __init__(self,n):
        self.V=n
        self.graph=[[] for _ in range(n)]

    def add_edge(self,u,v):
        self.graph[u].append(v),self.graph[v].append(u)

    def is_safe(self, vertex, color, color_map):
        for neighbor in self.graph[vertex]:
            if color_map.get(neighbor) == color:
                return False
        return True

    def color_graph(self, vertex, num_colors, color_map):
        if vertex == self.V:
            return True
        for color in range(num_colors):
            if self.is_safe(vertex, color, color_map):
                color_map[vertex] = color
                if self.color_graph(vertex + 1, num_colors, color_map):
                    return True
                color_map[vertex] = -1
        return False

    def backtracking_coloring(self):
        color_map = {-1: -1}
        num_colors = 1
        while not self.color_graph(0, num_colors, color_map):
            num_colors += 1
            color_map = {-1: -1}
        return num_colors

def color(grid):
    a,g,u,r,q=[i.strip() for i in grid.splitlines() if i],{},set(),set(),set()
    n,m=len(a),len(a[0])
    def dfs(i,j,k):
        if i<0 or i>=n or j<0 or j>=m or (i,j) in u:
            return
        if a[i][j]!=k:
            r.add(a[i][j])
            return
        u.add((i,j))
        dfs(i+1,j,k),dfs(i-1,j,k),dfs(i,j+1,k),dfs(i,j-1,k)
    for i in range(n):
        for j in range(m):
            if a[i][j] not in q:
                dfs(i,j,a[i][j])
                g[a[i][j]]=r
                r=set()
                u.clear()
                q.add(a[i][j])
    x=list(set(sum([list(g[i]) for i in g],[])))
    graph=Graph(len(x))
    d={x[i]:i for i in range(len(x))}
    for i in g:
        for j in g[i]:
            graph.add_edge(d[i],d[j])
    return graph.backtracking_coloring()

print(color("""
AAAAAA
ABBCCA
ABDECA
ABDDCA
AAAAAA
"""))