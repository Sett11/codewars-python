def gen_sn(n):
    r,i=list(range(1,n+1,2)),1
    for i in range(3,int(n**.5)):
        del r[i-1::i]
    return r

s_n=set(gen_sn(10**8))

def survivor(n):
    return n in s_n

print(survivor(289))