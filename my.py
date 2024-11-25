def reduce_by_rules(lst,r):
    a,i=lst[::-1],0
    while len(a)>1:
        a.append(r[i%len(r)](a.pop(),a.pop()))
        i+=1
    return a[0]

rules = [lambda a, b: a + b, lambda a, b: a - b]
print(reduce_by_rules([2.0, 2.0, 3.0, 4.0],rules))