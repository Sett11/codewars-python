from datetime import timedelta

def sort_time(a):
    n=len(a)
    g=next(i for i,j in enumerate(a) if j[0]==min([i[0] for i in a]))
    a.insert(0,a.pop(g))
    for i in range(n):
        h,mi=map(int,a[i][1].split(':'))
        d,m,x,d2={},1e9,timedelta(hours=h,minutes=mi),{}
        for j in range(i+1,n):
            h,mi=map(int,a[j][0].split(':'))
            y=timedelta(hours=h,minutes=mi)
            q=y-x
            if x<=y:
                z=q.seconds
                if z not in d:
                    d[z]=j
                    m=min(m,z)
            else:
                z=q.seconds
                if -z not in d2:
                    d2[-z]=j
        if d:
            a.insert(i+1,a.pop(d[m]))
        else:
            if d2:
                v=max(d2)
                a.insert(i+1,a.pop(d2[v]))
    return a

print(sort_time([['15:54', '21:53'], ['16:03', '15:54'], ['12:50', '00:14'], ['08:06', '12:39'], ['01:40', '07:15'], ['15:54', '21:15'], ['20:07', '11:32'], ['04:17', '00:30'], ['00:46', '20:12'], ['13:04', '06:49'], ['20:41', '21:53'], ['08:34', '12:56'], ['15:43', '23:25'], ['02:11', '16:34'], ['04:17', '12:39'], ['13:20', '18:59'], ['21:15', '08:09']]))