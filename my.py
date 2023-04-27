def reverse_factorial(n):
    if(n==1):
        return '1!'
    i=1
    while True:
        if(n==1.0):
            return str(int(n*i-1))+'!'
        if(n<=0):
            break
        n/=i
        i+=1
    return 'None'
    
print(reverse_factorial(120))