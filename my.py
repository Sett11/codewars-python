def elements_sum(a,d=0):
    s=0
    l=len(a)-1
    for i in a:
        if(l>len(i)-1):
            s+=d
            l-=1
        else:
            s+=i[l]
            l-=1
    return s

print(elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []]))