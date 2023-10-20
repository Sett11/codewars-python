def check(n):
    try: return not next(i for i in range(2,int(n**.5)+1) if not n%i)
    except: return n>1

def next_prime(n):
    x=n+1
    while True:
        if check(x):
            return x
        x+=1

print(next_prime(10**10))