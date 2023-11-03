def new_numeral_system(n):
    s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n=s.index(n)
    r=[]
    for i in range(25):
        for j in range(i,25):
            if i+j==n:
                r.append(f'{s[i]} + {s[j]}')
    return r


print(new_numeral_system('O'))