def max_sequence(a):
    m=n=0
    for i in a:
        n+=i
        if n>m:
            m=n
        if n<0:
            n=0
    return m

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))