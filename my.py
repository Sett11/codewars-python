def solve(a,b):
    if(len(b)>len(a)):
        return 0
    for i in b:
        if(i not in a or b.count(i)>a.count(i)):
            return 0
    a=list(a)
    b=list(b)
    while len(b):
        t=b.pop(0)
        a.remove(t)
    return len(a)

print(solve("aabcdefg","fbd"))