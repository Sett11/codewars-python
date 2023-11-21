def f(a,b):
    m,n=a,b

    while m!=n:
        if m>n:
            n+=b
        else:
            m+=a

    return m

def sum_differences_between_products_and_LCMs(a):
    return sum([i*j-f(i,j) for i,j in a])

print(sum_differences_between_products_and_LCMs([[15,18], [4,5], [12,60]]))