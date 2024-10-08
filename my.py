import networkx as nx
import numpy as np

class Graph():
    def __init__(self,n):
        self.v=n
        self.mat=[[0]*self.v for _ in range(self.v)]
        self.nodes=None

    def adjmat_2_graph(self,a):
        g={}
        for i in range(self.v):
            key=f'A{i}'
            g[key]=[]
            for j in range(self.v):
                if a[i][j]:
                    g[key].append((f'A{j}',a[i][j]))
            g[key]=sorted(sorted(g[key],key=str),key=len)
        return g
        
    def graph_2_mat(self,g):
        for i in g:
            for j,k in g[i]:
                self.mat[int(i[1:])][int(j[1:])]=k
        return self.mat
    
    def graph_2_list(self,g):
        return sorted(sorted([list(i) for i in g.items()],key=str),key=len)
        
    def list_2_graph(self,a):
        return dict(a)
        
    def mat_2_list(self,a):
        return self.graph_2_list(self.adjmat_2_graph(a))
    
    def list_2_mat(self,a):
        return self.graph_2_mat(self.list_2_graph(a))

    def find_all_paths(self,g,s,e):
        if s==e:
            return [s]
        g=nx.from_numpy_array(np.array(self.graph_2_mat(g)),create_using=nx.DiGraph)
        return sorted(sorted(['-'.join(f'A{j}' for j in i) for i in nx.all_simple_paths(g,int(s[1:]),int(e[1:]))],key=str),key=len)


# o = [[0, 0, 4, 0, 1],[2, 0, 3, 8, 5],[0, 3, 0, 0, 7],[6, 8, 0, 0, 9],[0, 5, 7, 9, 0]]
# g = Graph(5)

# print(g.adjmat_2_graph(o))
# print(g.list_2_mat([['A0', [('A2', 4), ('A4', 1)]], ['A1', [('A0', 2), ('A2', 3), ('A3', 8), ('A4', 5)]], ['A2', [('A1', 3), ('A4', 7)]], ['A3', [('A0', 6), ('A1', 8), ('A4', 9)]], ['A4', [('A1', 5), ('A2', 7), ('A3', 9)]]]))
# print(g.graph_2_list({'A0': [('A4', 1), ('A2', 4)], 'A1': [('A0', 2), ('A2', 3), ('A4', 5), ('A3', 8)], 'A2': [('A1', 3), ('A4', 7)], 'A3': [('A0', 6), ('A1', 8), ('A4', 9)], 'A4': [('A1', 5), ('A2', 7), ('A3', 9)]}))
# print(g.list_2_graph([['A0', [('A4', 1), ('A2', 4)]], ['A1', [('A0', 2), ('A2', 3), ('A4', 5), ('A3', 8)]], ['A2', [('A1', 3), ('A4', 7)]], ['A3', [('A0', 6), ('A1', 8), ('A4', 9)]], ['A4', [('A1', 5), ('A2', 7), ('A3', 9)]]]))
g=Graph(6)
print(g.find_all_paths({'A5': [('A3', 1)], 'A3': [('A0', 1), ('A2', 1)], 'A0': [('A3', 1), ('A5', 1)], 'A4': [('A2', 1)], 'A1': [('A2', 1)], 'A2': [('A1', 1), ('A2', 1), ('A3', 1), ('A4', 1)]},'A0','A5'))