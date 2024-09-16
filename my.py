def judge(a):
    r=[30-i for i,j in enumerate(zip(*[bin(i)[2:].rjust(30,'0') for i in a])) if all(k=='1' for k in j)]
    return r[0] if len(r)==1 else 0

print(judge([7, 15, 4])) 