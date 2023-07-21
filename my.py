def draw(d):
    a=[]
    while len(d):
        a.append(d.pop(0))
        if len(d):
            d.append(d.pop(0))
    return a

print(draw(['AH','2H','3H','4H']))