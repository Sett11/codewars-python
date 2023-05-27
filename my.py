def custom_fib(s,j,n):
    while len(s)<=n:
        s.append(sum([s[i] for i in j]))
        j=[i+1 for i in j]
    return s[n]

print(custom_fib([1,1],[0,1],4))
print(custom_fib([3,5,2],[0,1,2],4))
print(custom_fib([7,3,4,1],[1,1],6))