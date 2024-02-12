from statistics import mean,median

def f(n):
    a=[{1.}]
    for i in range(1,n+1):
        a.append({(i-x)*j for x,s in enumerate(a) for j in s})
    return sorted(a[-1])

def part(n):
    a=f(n)
    b,c,d=a[-1]-a[0],mean(a),median(a)
    return f"Range: {'{:.2f}'.format(b) if b and b%1 else int(b)} Average: {'{:.2f}'.format(c) if c else int(c)} Median: {'{:.2f}'.format(d) if d else int(d)}"

print(part(10))