def get_score(n):
    a,b,c=50,100,0

    while c<n-1:
        a+=b
        b+=50
        c+=1
    
    return a

print(get_score(1002))