class Node:
    def __init__(self,next=None):
        self.next=next

def loop_size(head):
    a,c=[],set()
    h=head
    while h:
        if h in c:
            return len(a)-a.index(h)
        a.append(h)
        c.add(h)
        h=h.next


node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(loop_size(node1))