def sum_of_a_beach(s):
    a,c=["sand","water","fish","sun" ],0
    s=s.lower()
    while any(i in s for i in a):
        for i in a:
            if i in s:
                s=s.replace(i,'',1)
                c+=1
    return c

print(sum_of_a_beach('123FISH321'))