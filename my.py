def f(s):
    a=b=''
    for i,j in enumerate(s):
        if i&1:
            b+=j
        else:
            a+=j
    return a+b

def jumbled_string(s,n):
    c,i=s,0
    while True:
        c=f(c)
        i+=1
        if c==s:
            break
    n%=i
    while n:
        c=f(c)
        n-=1
    return c
    

print(jumbled_string('gwr93VO?UUu}_LIqmO`TbODl1fa{PA^l9tJh_7yLE1XteXd>HiuiBuI@V5TL62DB[=BE6:NlM{[TboTmgL<CmonV:;EG0OmCmL5O',1897))