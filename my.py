def baubles_on_tree(a,b):
    if(not b):return 'Grandma, we will have to buy a Christmas tree first!'
    r=list(map(lambda e:0,list(range(b))))
    i=0
    while a:
        r[i%len(r)]+=1
        a-=1
        i+=1
    return r

print(baubles_on_tree(12,5))