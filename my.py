def reverse_list(h):
    if not h:
        return
    r=[]
    while h:
        r.append(h.value)
        h=h.next
    h=c=Node(None,None)
    while len(r)>1:
        c.value=r.pop()
        c.next=Node(None,None)
        c=c.next
    c.value=r[0] if r else None
    return h