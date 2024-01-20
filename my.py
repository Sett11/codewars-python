count_number=lambda n,x: len([i for i in range(1,n+1) if x%i==0 and x//i<=n])
        


print(count_number(100000,1000000000))