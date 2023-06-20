def triple_trouble(o,t,h):
    s,i='',0
    while i<len(o):
        s+=o[i]+t[i]+h[i]
        i+=1
    return s

print(triple_trouble("burn", "reds", "roll"))