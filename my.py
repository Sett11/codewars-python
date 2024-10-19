def leaderboard_sort(a,b):
    for i in b:
        x,y=i.split()
        k,p=int(y),a.index(x)
        while k:
            t=p-1 if k>0 else p+1
            a[p],a[t]=a[t],a[p]
            k=k+1 if k<0 else k-1
            p=t
    return a

print(leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1']))
print(leaderboard_sort(['Bob', 'Larry', 'Kevin', 'Jack', 'Max'], ['Max +3', 'Kevin -1', 'Kevin +3']))