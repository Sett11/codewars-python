from gmpy2 import is_prime

a=[0,1,1,2,4]
r=[]

def kth_last_dig_prime(k):
    while len(r)<k:
        x=a[-1]+a[-2]-a[-3]+a[-4]-a[-5]
        a.append(x)
        s=str(x)
        if len(s)>9 and is_prime(int(s[-9:])):
            r.append([len(a),int(s[-9:])])
    return r[k-1]

print(kth_last_dig_prime(5))
print(kth_last_dig_prime(112))
print(kth_last_dig_prime(10))