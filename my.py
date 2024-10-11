def fill(a,d=0):
    def f(a,i,d):
        if a[i] is not None:
            return a[i]
        if d==-1:
            i+=1
            while i<len(a):
                if a[i] is not None:
                    return a[i]
                i+=1
            return
        if d==1:
            i-=1
            while i>=0:
                if a[i] is not None:
                    return a[i]
                i-=1
            return
        else:
            k,r=i,[]
            i+=1
            while i<len(a):
                if a[i] is not None:
                    r.append((abs(k-i),a[i]))
                    break
                i+=1
            i=k-1
            while i>=0:
                if a[i] is not None:
                    r.append((abs(k-i),a[i]))
                    break
                i-=1
            if r:
                return sorted(r)[0][1]
    r=[None]*len(a)
    for i in range(len(a)):
        r[i]=f(a,i,d)
    return r

print(fill([None, 1, None, None, None, 2, None],0))