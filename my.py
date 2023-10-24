def divisions(n,d,c=0):
    return c if n<=1 or n<d else divisions(n//d,d,c+1)

print(divisions(100,2))