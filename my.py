def two_by_two(a):
    b,r=set([i for i in a if a.count(i)>=2]),{}
    for i in b:
        r[i]=2
    return r if a else False

print(two_by_two(["dog", "cat", "dog", "cat", "beaver", "cat"]))