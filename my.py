from collections import defaultdict
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

a,b,c,d,e,f,j=[Node(chr(i+64)) for i in range(1,8)]
a.left=b
a.right=c
b.left=d
c.left=e
b.right=f
c.right=j

def serpentine_traversal(h):
    d,i=defaultdict(list),0
    def f(x):
        nonlocal i
        if not x:
            return
        d[i].append(x.data)
        i+=1
        f(x.left)
        f(x.right)
        i-=1
    f(h)
    return sum([j[1][::-1] if i&1 else j[1] for i,j in enumerate(d.items())],[])

print(serpentine_traversal(a))