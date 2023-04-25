class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(h,d):
    r=None
    r=Node(d)
    r.next=h
    return r
  
def build_one_two_three():
    t=None
    t=push(t,3)
    t=push(t,2)
    t=push(t,1)
    return t