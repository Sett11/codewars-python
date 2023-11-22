def clock(n,a):
    r=[]
    s=set()
    j=0

    for i in a:

        if i in s:
            for k in range(n):
                if r[k][0]==i:
                    r[k][1]=1
                    break

        if len(r)<n and i not in s:
            r.append([i,0])
            s.add(i)
            j+=1

        if len(r)==n and i not in s:

            while True:
                if not r[j%n][1]:
                    break
                else:
                    r[j%n][1]=0
                j+=1

            s.remove(r[j%n][0])
            r[j%n]=[i,0]
            s.add(i)
            j+=1

    r=[i for i,j in r]
    return r+[-1]*(n-len(r))

print(clock(3,[6, 3, 6, 3, 2, 5, 1, 6]))
print(clock(4,[1, 2, 3, 4, 5, 5, 3, 6, 7, 8]))
print(clock(3, [1, 2, 3, 4, 2, 5]))