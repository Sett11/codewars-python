from sys import set_int_max_str_digits
set_int_max_str_digits(1000000)

def fib(n):

    def f(x):
        if not x:
            return [0,1]
        if x==1:
            return [1,1]
        a,b=f(x//2)
        p,q=a*(2*b-a),b*b+a*a
        return [p,q] if x%2==0 else [q,p+q]

    return f(n)[0] if n>=0 else -f(-n)[0] if n%2==0 else f(-n)[0]


print(fib(-96))
print(fib(1000000))