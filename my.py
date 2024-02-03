def cant_beat_so_join(a):
    return sum(sorted(a,key=sum,reverse=True),[])

print(cant_beat_so_join([[1,2], [3,4], [5,6], [7,8], [9]]))