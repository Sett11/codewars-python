from collections import deque


def lru(n,a):
    q=deque()
    c=q.copy()

    for i in a:
        if len(q)>=n:
            if i in q:
                c.remove(i)
                c.append(i)
            else:
                q[q.index(c[0])]=i
                c.remove(c[0])
                c.append(i)
        else:
            if i in q:
                c.remove(i)
                c.append(i)
            else:
                q.append(i)
                c.append(i)

    return list(q)+[-1]*(n-len(q))


print(lru(3,[1, 2, 3, 4, 3, 2, 5]))
print(lru(4,[5, 4, 3, 2, 3, 5, 2, 6, 7, 8]))
print(lru(3,[1,1,1]))