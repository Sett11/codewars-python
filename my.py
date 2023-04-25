def play_if_enough(h,p):
    r=h
    p=list(p)
    h=list(h)
    while len(p):
        t=p.pop(0)
        if(t not in h):
            return (False,r)
        h.remove(t)
    return (True,''.join(h))

print(play_if_enough("oogssbbb", "bwsg"))