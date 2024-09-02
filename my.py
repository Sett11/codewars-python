# from random import choice
# from itertools import product

# u=set([tuple(i) for i in product([0,1],repeat=9)]+[tuple(i) for i in product([0,1],repeat=9)])
# u_list=list(u)

# def move(grid,k):
#    n=len(grid)
#    res,new_grid=[],grid.copy()
#    while k:
#       for i in range(n):
#          for j in range(n):
#             t=[(r,c) for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),(i+1,j+1),(i-1,j-1),(i+1,j-1),(i-1,j+1)] if r>=0 and r<n and c>=0 and c<n]
#             res.append((i,j,[grid[r][c] for r,c in t].count(1)))
#       for i,j,k in res:
#          if grid[i][j]==1 and (k>3 or k<2):
#             new_grid[i][j]=0
#          if grid[i][j]==0 and k==3:
#             new_grid[i][j]=1
#       grid=new_grid
#       k-=1
#       return grid

# def f(a):
#    return '\n'.join(list(''.join(str(j) for j in i) for i in a))

# def shange(a):
#    return [list(a[i:i+3]) for i in range(0,9,3)]

# x=shange(choice(u_list))
# for i in u:
#    x=move(shange(i),1)
#    t=[]
#    for j in u:
#       if i!=j:
#          y=move(shange(j),1)
#          if y==x:
#             t.append(shange(j))
#    if len(t)>1:
#       print(f(shange(i)),[f(k) for k in t])
#       break


import asyncio

async def dreaming(n,m):
    await asyncio.sleep(n)
    return m ** n 