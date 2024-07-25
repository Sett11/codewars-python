from queue import Queue

class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = [] if child_nodes is None else child_nodes

def tree_to_list(h):
    q,r=Queue(),[]
    q.put(h)
    while q.qsize():
        v=q.get()
        if v:
            r.append(v.data)
            for i in v.child_nodes:
                q.put(i)
    return r


print(tree_to_list(Node('H', [Node('e', [Node('l'), Node('o', [Node('w'), Node('!')])]), Node('l')])))