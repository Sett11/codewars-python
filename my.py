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
    
def reverse(a):
    return array_convert_to_list(list_convert_to_array(a)[::-1],a) if a else None
    

print(reverse(array_convert_to_list([1,2])))