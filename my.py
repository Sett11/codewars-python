def scratch(a):
    t=0
    for i in a:
        s=i.split()
        if s[0]==s[1]==s[2]:
            t+=int(s[3])
    return t

print(scratch(["tiger tiger tiger 100","rabbit dragon snake 100","rat ox pig 1000","dog cock sheep 10","horse monkey rat 5","dog dog dog 1000"]))