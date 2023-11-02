from collections import OrderedDict

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

def remove_duplicates(h):
    return array_convert_to_list(list(OrderedDict.fromkeys(list_convert_to_array(h)))) if h else None

print(remove_duplicates(array_convert_to_list([1,5,5,3,2])))