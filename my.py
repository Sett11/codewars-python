import numpy as np
import networkx as nx

def maximum_clique(a):
    if not a:
        return []
    g=nx.from_numpy_array(np.array(a),create_using=nx.Graph)
    return max(nx.algorithms.find_cliques(g),key=len)

print(maximum_clique([
      [0,1,0,0],
      [1,0,1,1],
      [0,1,0,1],
      [0,1,1,0]
    ]))
print(maximum_clique([
      [0,0,0,1,0,1], 
      [0,0,1,0,1,0], 
      [0,1,0,1,0,0], 
      [1,0,1,0,1,1], 
      [0,1,0,1,0,0], 
      [1,0,0,1,0,0]
    ]))