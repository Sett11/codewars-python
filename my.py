def christmas_tree(x):
    n=x//3
    a=['*','***','*****']
    b=a
    while n>1:
        b=['*'+i+'*' for i in b]
        a.extend(b)
        n-=1
    m=max([len(i) for i in a])
    return '' if x<3 else '\r\n'.join([' '*((m//2)-len(i)//2)+i for i in a])+'\r\n'+' '*((m//2)-1)+'###'

print(christmas_tree(17))