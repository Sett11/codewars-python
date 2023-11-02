class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def list_convert_to_array(h):
    r=[]
    c=h
    while c:
        r.append(c.data)
        c=c.next
    return r

def array_convert_to_list(a):
    L=Node(0)
    c=L
    l=len(a)
    for i in range(l):
            c.data=a[i]
            c.next=Node(0) if i!=l-1 else None
            c=c.next
    return L
    
def alternating_split(h):
    a=list_convert_to_array(h)
    n=len(a)
    if n<2:
        raise()
    return Context(array_convert_to_list(a[0:n:2]),array_convert_to_list(a[1:n:2]))

print(alternating_split(array_convert_to_list([1,2,3,4,5])))