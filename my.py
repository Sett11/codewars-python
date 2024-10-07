import networkx as nx

def path_finder(a):
    g=nx.Graph()
    a=a.splitlines()
    n,m=len(a),len(a[0])
    for i in range(n):
        for j in range(m):
            if a[i][j]=='.':
                for k in [(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0<=x<n and 0<=y<m and a[x][y]=='.']:
                    g.add_edge((i,j),k)
    r=g,(0,0),(n-1,m-1)
    if r[-1] not in g or r[1] not in g or not nx.has_path(*r):
        return False
    return nx.shortest_path_length(*r)

print(path_finder("\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])))