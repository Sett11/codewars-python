import networkx as nx

def shortest_path(a,s,e):
    g=nx.DiGraph()
    [[g.add_edge(i,j,weight=a[i][j]) for j in a[i]] for i in a]
    p=sorted(nx.all_shortest_paths(g,s,e,weight=lambda x,y,_:g[x][y]['weight']))
    return [i for i in p if len(i)==len(min(p,key=len))]

print(shortest_path({'a' : {'b': 10, 'c': 20, 'e':20},
            'b' : {'a': 10, 'd': 20},
            'c' : {'a': 10, 'f': 20},
            'd' : {'b': 10, 'e': 20, 'g': 20},
            'e' : {'a': 10, 'd': 20, 'f': 20},                      
            'f' : {'c': 10, 'e': 20, 'h': 20},
            'g' : {'d': 10, 'h': 20},
            'h' : {'g': 10, 'f': 20},
},'a','f'))