def f(s):
    a,b,c=map(int,s.split(':'))
    return a*3600+b*60+c

def video_part(n,t):
    k,c=f(t)/f(n),1
    while 1:
        x=round(k*c,5)
        if x==int(x):
            return [c,int(x)]
        c+=1

print(video_part('08:27:48','96:28:48'))
print(video_part('00:48:32','03:24:32'))