def equable_triangle(a,b,c):
    p=(a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**.5==p*2

print(equable_triangle(5,12,13))
print(equable_triangle(73,9,80))