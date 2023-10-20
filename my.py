def check(n):
    try: return not next(i for i in range(2,int(n**.5)+1) if not n%i)
    except: return n>1

def prime_primes(n):
    a=[i for i in range(2,n) if check(i)]
    r=[]
    c=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            r.append(a[i]/a[j])
            c+=1
    return c,int(sum(r))


print(prime_primes(6))