from itertools import zip_longest

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
def list_convert_to_array(h):
    r=[]
    c=h
    while c:
        r.append(c.data)
        c=c.next
    return r

def array_convert_to_list(a,L=None):
    L=L or Node(0)
    c=L
    l=len(a)
    for i in range(l):
            c.data=a[i]
            c.next=Node(0) if i!=l-1 else None
            c=c.next
    return L
    
def shuffle_merge(f,s):
    if f is None: return s
    if s is None: return f
    return array_convert_to_list([k for k in sum([list(i) for i in zip_longest(list_convert_to_array(f),list_convert_to_array(s))],[]) if k])
    

print(shuffle_merge(array_convert_to_list([1,2,3,4,5,6]),array_convert_to_list([9,10,11])))