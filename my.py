class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

a = Node("A")
b = Node("B")
c = Node("C")
  
a.left = b
a.right = c


def pre_order(n):
    r=[]
    def f(h):
        if not h:
            return
        r.append(h.data)
        f(h.left)
        f(h.right)
    f(n)
    return r

def in_order(n):
    r=[]
    def f(h):
        if not h:
            return
        f(h.left)
        r.append(h.data)
        f(h.right)
    f(n)
    return r

def post_order(n):
    r=[]
    def f(h):
        if not h:
            return
        f(h.left)
        f(h.right)
        r.append(h.data)
    f(n)
    return r

print(pre_order(a))
print(in_order(a))
print(post_order(a))