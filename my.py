f=lambda n:n>=2 and all(n%i for i in range(2,int(n**.5)+1))

def number_property(n):
    return [f(n),n%2==0,n%10==0]

print(number_property(122))