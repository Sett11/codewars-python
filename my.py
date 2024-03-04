# def fusc(n):
#     assert type(n)==int and n>=0
#     return 0 if n==0 else 1 if n==1 else fusc(n//2) if n%2==0 else fusc(n//2)+fusc(n//2+1)
    
# print(fusc(10))

def fibfusc(n):
    def f(k):
        if k==0:
            return (1,0)
        if k==1:
            return (0,1)
        x,y=f(k//2)
        return ((x + y)*(x - y),y*(2*x + 3*y)) if k%2==0 else (-y*(2*x + 3*y), (x + 2*y)*(x + 4*y))
    return f(n)

print(fibfusc(5))