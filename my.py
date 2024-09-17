def who_eats_who(s):
    d={'antelope': ['grass'], 'big-fish': ['little-fish'], 'bug': ['leaves'], 'bear': ['big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'], 'chicken': ['bug'], 'cow': ['grass'], 'fox': ['chicken', 'sheep'], 'giraffe': ['leaves'], 'lion': ['antelope', 'cow'], 'panda': ['leaves'], 'sheep': ['grass']}
    a,r=s.split(','),[s]
    while len(a)>1:
        n,i=len(a),0
        while i<n:
            if a[i] in d:
                if i==0:
                    if a[i+1] in d[a[0]]:
                        r.append(f'{a[i]} eats {a.pop(i+1)}')
                        break
                elif i==n-1:
                    if a[i-1] in d[a[i]]:
                        r.append(f'{a[i]} eats {a.pop(i-1)}')
                        break
                else:
                    if a[i-1] in d[a[i]]:
                        r.append(f'{a[i]} eats {a.pop(i-1)}')
                        break
                    if a[i+1] in d[a[i]]:
                        r.append(f'{a[i]} eats {a.pop(i+1)}')
                        break
            i+=1
        else:
            break
    return r+[','.join(a)]

print(who_eats_who("fox,bug,chicken,grass,sheep"))