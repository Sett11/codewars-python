def powerof4(n):
    print(n)
    if(type(n)!=int):
        return False
    i=0
    while True:
        if(4**i==n):
            return True
        if(4**i>n):
            return False
        i+=1

print(powerof4(1))