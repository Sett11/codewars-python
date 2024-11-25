def paper_fold():
    s,i='1',0
    def f():
        nonlocal s
        s=s+'1'+''.join('0' if i=='1' else '1' for i in s[::-1])
    while True:
        yield int(s[i])
        i+=1
        if i==len(s):
            f()

g=paper_fold()
print([next(g) for _ in range(20)])