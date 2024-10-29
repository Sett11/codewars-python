from collections import deque

class Num(int):
    def __init__(self,n):
        self.n=n

    def __sub__(self,other):
        return Num(self.n-other)

def queue(a,i):
    a[i]=Num(a[i])
    q,c=deque(a),0
    while True:
        q[0]-=1
        c+=1
        if isinstance(q[0],Num) and not q[0]:
            return c
        elif not q[0]:
            q.popleft()
        else:
            q.append(q.popleft())
        

print(queue([2, 5, 3, 6, 4],1))
print(queue([2, 5, 3, 6, 4],4))
print(queue([2, 5, 3, 6, 4], 3))