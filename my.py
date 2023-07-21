def ball_test(s,r):
    c,i,x=0,0,0
    while i<len(r):
        if r[i]=='x':
            c+=1
        if x==s:
            s-=c+1
            x=-1
            c=0
        if s<1:
            return False
        if i==len(r)-1:
            return True
        i+=1
        x+=1

print(ball_test(5,'x___x__x'))