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

def insert_sort_to_list(a):
    for i in range(1,len(a)):
          k=i
          while k and a[k-1]>a[k]:
               a[k],a[k-1]=a[k-1],a[k]
               k-=1
    return a

def insert_sort(head):
    return array_convert_to_list(insert_sort_to_list(list_convert_to_array(head))) if head else None
    

print(insert_sort(array_convert_to_list([1,5,3,2])))