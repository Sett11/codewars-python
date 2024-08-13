def on_line(a):
    if len(a)<3 or len(set(i[0] for i in a))==1 or len(set(i[1] for i in a))==1:
        return True
    a=list(a)
    x=a.pop(0)
    a=list(filter(lambda y:not (x[0]==y[0] and x[1]==y[1]),a))
    try:
        for i in range(len(a)):
            a[i]=(x[0]-a[i][0])/(x[1]-a[i][1])
        return len(set(a))==1
    except:
        return False

print(on_line(((2,1), (4,1), (7,1))))