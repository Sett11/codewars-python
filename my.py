def alex_mistakes(n,t):
    t-=n*6
    c=5;i=0;j=0
    if(t==0):return t
    while j<t:
        j+=c;c*=2;i+=1
    return i if j==t else i-1

print(alex_mistakes(20,135))