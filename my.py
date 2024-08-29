# from math import log

# def li(x,n=100):
#     if x<2:
#         return float('nan')
#     step=(x-2)/n
#     integral=.0
#     for i in range(n):
#         t1,t2=2+i*step,2+(i+1)*step
#         if t1>0 and t2>0:
#             integral+=(1/log(t1)+1/log(t2))*step/2
#     return integral

# print(li(10000))

# def get_neighbourhood(t,a,c,d):
#     n,m,r,v=len(a),len(a[0]),[],t=='von_neumann'
#     if not m or not d or 0>c[0] or c[0]>=n or 0>c[1] or c[1]>=m:
#         return []
#     for i in range(c[0]-d+(1 if v else 0),c[0]+d-(1 if v else 0)+1):
#         for j in range(c[1]-d+(1 if v else 0),c[1]+d-(1 if v else 0)+1):
#             if (i,j)!=c and i>=0 and i<n and j>=0 and j<m:
#                 r.append(a[i][j])
#     if v:
#         z=[[c[0]-d,c[1]],[c[0]+d,c[1]],[c[0],c[1]-d],[c[0],c[1]+d]]
#         r.extend([a[i][j] for i,j in z if i>=0 and i<n and j>=0 and j<m])
#     return sorted(r)


# print(get_neighbourhood('von_neumann',[
#        [ -8,  -2,   6,  -5,   8,   0,   1,   6,   4,   4,   1,   9],
#         [  8,  -5,   2,  -4,  -1,  -7,   5,  -8, -10,   0,  -3,  -3],
#         [  7,  -3,   3,  -6,  -3, -10,  -2,  -6,  10,   7,  -7,  -1],
#         [ -3,  10,  -1,   0,  -4,   3,  -4,  -6,  -8,   4,  -6,   6],
#         [ -3,   3,  -6,   2,  -8,  -1,  -8,   1,   5,   6,   1,  -9],
#         [ -5,   2,   0,   8,  -8,  -9,   0,  -9,  -1,  -4,  -8,  -1],
#         [  9,  -4,   4, -10,   6,   4,  -5,  -7,   1,   2,   6, -10],
#         [-10, -10,   6,  -5,   7,   7,  -3,  -7,   9,   5,   7,  -5],
#         [ -4,   3,   9,   4,  -7,  -1,  -5,  -5,   9,   1,  -1,  -7],
#         [  7,  -6,  -2,   4,  -1,   5,   4,   4,  -3,   2,   4,  -5],
#         [ -4,  -7,   1,   2,   9,   5,  10,   5,  -6,   5,   8,   4],
#         [ -2,   4,   5,  10,  -4,   3,  -6,   8,   8,  -1,   9,  -3]],(11,2),3),sep='\n')

# [-7, -6, -4, -4, -2, -2, 1, 2, 3, 4, 4, 9, 9, 10]

from collections import Counter

def pyramid(a):
    d,c,r=Counter(a),0,[]
    for i in range(3,0,-1):
        t=[j for j in d.items() if j[1]>=i and j[0] not in r]
        if not t:
            return
        x=max(t)[0]
        c+=x*i
        d[x]-=i
        r.append(x)
    return c



print(pyramid([5,3,5,3,0,0,-1,0,0,3,3,3]))