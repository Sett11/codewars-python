import networkx as nx

def path_finder(area):
    g,a=nx.Graph(),area.splitlines()
    n,m=len(a),len(a[0])
    if [n,m]==[1]*2:
        return 0
    for i in range(n):
        for j in range(m):
            for x,y in [(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0<=x<n and 0<=y<m]:
                g.add_edge((i,j),(x,y),weight=abs(int(a[i][j])-int(a[x][y])))
    path=nx.shortest_path(g,(0,0),(n-1,m-1),lambda x,y,_:g[x][y]['weight'])
    return sum(g[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))

print(path_finder("\n".join([
          "1"
        ])))