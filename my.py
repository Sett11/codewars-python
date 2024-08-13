import networkx as nx
from itertools import product

def processes(s,e,p):
    g={j:[] for _,j,__ in p}
    for i in g:
        for j in p:
            if i==j[1]:
                if j[-1] not in g[i]:
                    g[i].append(j[-1])
    try:
        G=nx.DiGraph()
        G.add_nodes_from([i for i in g])
        G.add_edges_from(sum([list(product([i],g[i])) for i in g],[]))
        path,r=nx.shortest_path(G,s,e),[]
        for i in range(len(path)-1):
            t=(path[i],path[i+1])
            for j in p:
                if j[1:]==t:
                    r.append(j[0])
        return r
    except:
        return []

print(processes('0', '16', [('em', '0', '1'), ('qw', '5', '9'), ('qz', '6', '11'), ('nh', '11', '12'), ('qh', '3', '6'), ('mk', '8', '11'), ('rb', '3', '8'), ('fl', '12', '14'), ('hb', '2', '6'), ('er', '13', '16'), ('vx', '9', '10'), ('lh', '4', '8'), ('vk', '12', '15'), ('qc', '9', '12'), ('dr', '12', '16'), ('pl', '1', '3'), ('xc', '5', '7'), ('et', '9', '12'), ('zj', '3', '5'), ('tm', '6', '8'), ('bt', '12', '13'), ('fk', '8', '13'), ('wp', '8', '9'), ('ab', '10', '11'), ('lt', '10', '15'), ('qd', '7', '10'), ('ng', '1', '2')]))