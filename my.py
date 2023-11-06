def match(a,n):
    a=sum(a)
    c=100
    while n:
        c-=c/100*15
        n-=1
    return ['No match!','Match!'][a>=c]

print(match([26,23,19],3))