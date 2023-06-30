def has_exit(m):
    if(''.join(m).count('k')!=1):
        raise()
    if len(m)==1:
        return True
    n,i=max([len(i) for i in m]),0
    while i<len(m):
        while len(m[i])<n:
            m[i]+=' '
        i+=1
    a,n,c=[i for i in [[[j,i] for i,k in enumerate(h) if k==' '] for j,h in enumerate(m)] if len(i)],[i[0] for i in [[[j,i] for i,k in enumerate(h) if k=='k'] for j,h in enumerate(m)] if len(i)],[]
    [c.extend(i) for i in a]
    x=[i for i in c if i[1]==len(m[0])-1 or i[1]==0 or i[0]==0 or i[0]==len(m)-1]
    if not len(x):
        return False
    i,t=0,[]
    while i<len(n):
        k=n[i]
        t=[i for i in c if i[0]==k[0]-1 and i[1]==k[1] or i[0]==k[0] and i[1]==k[1]-1 or i[0]==k[0]+1 and i[1]==k[1] or i[0]==k[0] and i[1]==k[1]+1]
        if len([i for i in t if i in x]):
            return True
        if not len(t) and i==len(n)-1:
            break
        c=[i for i in c if i not in t]
        n=[i for i in n if i!=k]
        n+=t
        i=0
    return len([i for i in n if i in x])>0

print(has_exit([
    "########",
    "# # ####",
    "# #k#   ",
    "# # # ##",
    "# # # ##",
    "#      #",
    "########"]))
print(has_exit(['#   # #  #',
                '# #    # #',
                '##  # ## #',
                ' # #     #',
                '# #  ### #',
                ' ### k## #',
                '##   #   #',
                ' ### ##  #',
                '   # # # #',
                '   ###   #'
                ]))