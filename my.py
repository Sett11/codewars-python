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
    
def sorted_intersect(a,b):
    r=sorted(set(list_convert_to_array(a))&set(list_convert_to_array(b)))
    return array_convert_to_list(r) if a and b and r else None
    

print(sorted_intersect(array_convert_to_list([1,2,44,4,5,6]),array_convert_to_list([99])))