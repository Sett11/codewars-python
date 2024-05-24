def possibly_perfect(a,b):
    x=y=0
    n=len(a)
    for i in range(n):
        if a[i]==b[i] or a[i]=='_':
            x+=1
        else:
            y+=1
    return x==n or x==a.count('_')

print(possibly_perfect(["A", "_", "C", "_", "B"],["A", "D", "C", "E", "B"]))
print(possibly_perfect(["T", "_", "F", "F", "F"],["F", "F", "T", "T", "T"]))
print(possibly_perfect(["B", "_", "B"],["B", "D", "C"]))