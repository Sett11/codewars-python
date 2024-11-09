def tree_photography(a):
    def f(a):
        m,c=a[0],0
        for i in a[1:]:
            if i>m:
                c+=1
                m=i
        return c
    return 'left' if f(a)>f(a[::-1]) else 'right'

print(tree_photography([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2]))