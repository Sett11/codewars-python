def max_int_chain(n):
    v=n&1
    return n//2*(n//2+(1 if v else 0))-(0 if v else 1) if n>=5 else -1

print(max_int_chain(10))