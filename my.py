from bisect import insort

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

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

def sorted_insert(head, data):
    a=list_convert_to_array(head)
    insort(a,data)
    return array_convert_to_list(a)

print(sorted_insert(array_convert_to_list([1,2,5]),4))