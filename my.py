def swap_cards(n1, n2):
    a,b=list(map(int,str(n1))),list(map(int,str(n2)))
    i=a.index(min(a))
    a[i],b[0]=b[0],a[i]
    return int(''.join(map(str,a)))>int(''.join(map(str,b)))

print(swap_cards(41,98))
print(swap_cards(67,53))