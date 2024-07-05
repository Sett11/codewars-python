def f(n):
   n%=60
   a,b=0,1
   if n==0:
       return 0
   if n==1:
       return 1
   for _ in range(2,n+1):
        a,b=b,(a+b)%60
   return b

def fibonacci_squared_sum(n):
    return (f(n)*f(n+1))%10
    
print(fibonacci_squared_sum(1000000000000000000))