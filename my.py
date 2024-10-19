def monty_hall(n,a):
    return round(100-100*len([i for i in a if i==n])/len(a))

print(monty_hall(2, [2,1,2,1,2,3,1,1,2,2,3]))