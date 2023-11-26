def smallest_doll_size(a):
    r=[]
    while not a is None:
        r.append(a.size)
        a=a()
    return r[-1] if r else a.size