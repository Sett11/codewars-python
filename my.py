from collections import defaultdict

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(h):
    d,i=defaultdict(list),0
    def f(x):
        nonlocal i
        if not x:
            return
        d[i].append(x.value)
        i+=1
        f(x.left)
        f(x.right)
        i-=1
    f(h)
    return sum([j for _,j in d.items()],[])

print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))