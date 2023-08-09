def asterisc_it(n): 
    i,a,s=0,list(str(n)) if type(n)!=list else list(''.join([str(i) for i in n])),'02468'
    while i<len(a)-1:
        if a[i] in s and a[i+1] in s:
            a=a[:i+1]+['*']+a[i+1:]
        i+=1
    return ''.join(a)

print(asterisc_it([1, 4, 64, 68, 67, 23, 1]))