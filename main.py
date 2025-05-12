def animals(x, y):
    if not (x or y):
        return 0,0
    co=0
    while y>=0:
        if x*2==y:
            return x,co
        y-=4
        x-=1
        co+=1
    return 'No solutions'

print(animals(72, 200))