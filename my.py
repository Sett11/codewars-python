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
    
def front_back_split(h,f,q):
    a=list_convert_to_array(h)
    n=len(a)
    if n<2:
        raise()
    b=a[:n//2]+([a[n//2]] if n&1 else [])
    c=a[n//2:]
    if n&1:
         c.pop(0)
    return list_convert_to_array(array_convert_to_list(b,f)),list_convert_to_array(array_convert_to_list(c,q))
    

print(front_back_split(array_convert_to_list([1,2,3,4,5,6,7,8,9,10,11]),Node(),Node()))