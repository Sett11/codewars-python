def factorial_division(n,d):
    r=1
    for i in range(n,d,-1):
        r*=i
    return r

print(factorial_division(8,5))