def height(n):
    h,r=2e6,0
    while n:
        h/=2.5
        r+=h
        n-=1
    a,b=str(round(r+2e6,3)).split('.')
    return f"{a}.{b.ljust(3,'0')}"

print(height(7))