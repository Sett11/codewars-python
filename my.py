from collections import deque

def ticker(s,w,c):
    n=len(s)
    a,b=deque([' ']*w),deque(s)
    while c:
        a.append(b.popleft()),b.append(a.popleft())
        c-=1
    return ''.join(a)

print(ticker('Hello world!', 10, 4))