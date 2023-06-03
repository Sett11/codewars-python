import sys
sys.set_int_max_str_digits(100000)
def fib_digits(n):
    a,b,c=0,1,0
    while n>0:
        n-=1;c=b;b+=a;a=c
    a=str(a)
    return sorted([(a.count(i),int(i)) for i in '0123456789' if a.count(i)],key=lambda e:(e[0],e[1]),reverse=True)

print(fib_digits(10000))