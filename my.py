from itertools import permutations,product

def solve_puzzle(a):
    n=len(a)//4
    z,p,r=[a[i:i+n] for i in range(0,len(a),n)],list(permutations(range(1,n+1))),[]
    for i in range(n):
        r.append([j for j in p if (count(j,n)==z[0][i] if z[0][i] else True) and (count(j[::-1],n)==z[2][::-1][i] if z[2][::-1][i] else True)])
    for i in list(product(*r)):
        t=list(zip(*i))
        if all(len(set(k))==n and (count(k[::-1],n)==z[1][j] if z[1][j] else True) and (count(k,n)==z[-1][::-1][j] if z[-1][::-1][j] else True) for j,k in enumerate(t)):
            return tuple(t)

def count(a,n):
    m=s=0
    for i in a:
        if i>m:
            s+=1
            m=i
        if i>n-1:
            break
    return s


print(solve_puzzle(( 0, 0, 1, 2,   
  0, 2, 0, 0,   
  0, 3, 0, 0, 
  0, 1, 0, 0 )
))