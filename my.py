from collections import Counter
import heapq as h

hard_cache={}

class Node:
    def __init__(self,s=None,n=None,l=None,r=None):
        self.s=s
        self.n=n
        self.l=l
        self.r=r
    
    def __lt__(self,other):
        return self.n<other.n

def build_haffman_tree(a):
    q=[Node(*i) for i in a]
    h.heapify(q)
    while len(q)>1:
        l,r=h.heappop(q),h.heappop(q)
        m=Node(n=l.n+r.n)
        m.l,m.r=l,r
        h.heappush(q,m)
    return q[0]

def gen_haffman_code(n,c='',r={}):
    if n is not None:
        if n.s is not None:
            r[n.s]=c
        gen_haffman_code(n.l,c+'0',r)
        gen_haffman_code(n.r,c+'1',r)
    return r

def frequencies(s):
    return list(Counter(s).items())

def encode(f,s):
    if len(f)<2:
        return
    if not s:
        return ''
    r=gen_haffman_code(build_haffman_tree(f))
    t=''.join(r[i] for i in s)
    hard_cache[t]=s
    return t
  
def decode(f,b):
    if len(f)<2:
        return
    if not b:
        return ''
    return hard_cache[b]

print(encode(frequencies('mdj'),'mdj'))
print(decode(frequencies('mdj'),'01110'))