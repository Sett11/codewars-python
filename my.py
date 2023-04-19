def polydivisible(x):
    x=list(str(x))
    i=1
    while i<=len(x):
        if(int(''.join(x[0:i]))%i!=0):
            return False
        i+=1
    return True

print(polydivisible(1232))