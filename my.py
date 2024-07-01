def number_of_sets(a,b):
    c=0
    for i in range(a):
        for j in range(i,a):
            for k in range(j,a):
                x,y=i+j+k,i*j*k
                if x>a or y>b:
                    break
                if x==a and y==b:
                    c+=1
    return c

print(number_of_sets(256,392150))
print(number_of_sets(137, 25200))