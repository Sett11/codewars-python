from re import sub
def solve(s):
    a,b,r=sorted(sub(r'[^aioue]','',s)),sorted(sub(r'[aioue]','',s)),[]
    if abs(len(a)-len(b))>1:
        return 'failed'
    if len(b)>len(a):
        a,b=b,a
    while a or b:
        r.append(a.pop(0))
        if b:
            r.append(b.pop(0))
    return ''.join(r)

print(solve('java'))
print(solve('have'))
print(solve('oruder'))
print(solve('apple'))
print(solve('wrhkrvfymtcddcwoiuoiiiioiuuiaoa'))