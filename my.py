def SumEvenFibonacci(n):
    if(n<=1):
        return 0
    if(n<8):
        return 2
    if(n<40):
        return 10
    a=b=c=1
    s=0
    while a<n:
        c=b
        b+=a
        a=c
        s+=0 if a%2!=0 else a
    return s


print(SumEvenFibonacci(7))