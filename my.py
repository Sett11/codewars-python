from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        r=[]
        def f(x):
            if not x:
                return
            f(x.left)
            r.append(str(x.value))
            f(x.right)
        f(self)
        return ' -> '.join(r)

def array_to_tree(a):
    if a:
        a=deque(a)
        x=Node(a.popleft())
        q=deque([x])
        while a:
            t=q.pop()
            t.left=Node(a.popleft())
            if not a:
                break
            t.right=Node(a.popleft())
            q.appendleft(t.left)
            q.appendleft(t.right)
        return x

print(array_to_tree([17, 0, -4, 3, 15]))
print(array_to_tree([]))