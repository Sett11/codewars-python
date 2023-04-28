def unlock(s):
    d={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
    c=''
    s=s.lower()
    for i in s:
        for j in d:
            if(i in d[j]):
                c+=str(j)
    return c

print(unlock('Valut'))