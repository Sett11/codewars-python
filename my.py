def cycle(d,v,c):
    v+=v
    try:
        return next(v[i+1] if d>0 else v[i-1] for i in range(len(v)) if v[i]==c)
    except:
        pass

print(cycle(1,[*range(0,70,3)],69))