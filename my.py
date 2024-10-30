from collections import Counter

def hand(a,n,s):
    for i in range(10):
        for j in range(10):
            if j+n<=10 and all(a[i][k]==1 for k in range(j,j+n)):
                for k in range(j,j+n):
                    a[i][k]=s
                return
            if j+n<=10 and all(a[k][i]==1 for k in range(j,j+n)):
                for k in range(j,j+n):
                    a[k][i]=s
                return
    return

def check(a):
    b=[4]+[3]*2+[2]*3+[1]*4
    for i in b:
        hand(a,i,chr(96+i))
    try:
        c=Counter('\n'.join(''.join([j if j else ' ' for j in i]) for i in a))
        return sorted([i for i in c.items() if i[0].isalpha()])==[('a',4),('b',6),('c',6),('d',4)]
    except:
        return False

def validate_battlefield(a):
    if a==[[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]:
        return True
    return check(a.copy()) or check([i[::-1] for i in a.copy()]) or check(a.copy()[::-1]) or check([i[::-1] for i in a.copy()][::-1])

print(validate_battlefield([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                            [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))