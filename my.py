import networkx as nx

def find_shortest_path(a,s,e):
    if not a:
        return a
    g,n,m=nx.Graph(),len(a),len(a[0])
    for i in range(n):
        for j in range(m):
            if a[i][j].passable:
                g.add_node((i,j))
                for k in [(k,p) for k,p in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if 0<=k<n and 0<=p<m and a[k][p].passable]:
                    g.add_edge((i,j),k)
    return [a[i][j] for i,j in nx.shortest_path(g,(s.position.x,s.position.y),(e.position.x,e.position.y))]