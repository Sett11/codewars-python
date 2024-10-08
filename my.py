import networkx as nx

def strongly_connected_components(a):
    g=nx.DiGraph()
    for i in range(len(a)):
        if not a[i]:
            g.add_node(i)
        for j in a[i]:
            g.add_edge(i,j)
    return list(nx.strongly_connected_components(g))

print(strongly_connected_components([[1], [2, 3, 4], [0, 3], [5], [5, 6], [3], [4, 7], [5, 6]]))
print(strongly_connected_components([[]]))