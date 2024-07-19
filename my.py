def find_min_cost(m,d,a):
    if d==1:
        y=min(a)
        if y<=m:
            return f'money: {y}'
        else:
            return f'days: 0'
    t=[]
    sm=ln=rl=0
    rs=1e9
    for i in range(len(a)):
        t.append(a[i])
        sm+=a[i]
        ln+=1
        while sm>m:
            x=t.pop(0)
            sm-=x
            ln-=1
            rl=max(rl,ln)
        if ln<d and sm<m:
            rl=max(rl,ln)
        if sm==m:
            rs=m
            rl=max(rl,ln)
            continue
        if ln==d:
            rs=min(rs,sm)
            rl=ln
        if ln>d:
            x=t.pop(0)
            sm-=x
            ln-=1
            rs=min(rs,sm)
    return f'money: {rs}' if rs<=m and rl==d else f'days: {rl}'


    

print(find_min_cost(100, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_min_cost(10,2,[3,7,6]))
print(find_min_cost(100, 5, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(find_min_cost(50,3,[10, 40, 5]))
print(find_min_cost(9,3,[10, 7, 3, 4]))