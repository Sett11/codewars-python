short=lambda x:{i:sum(map(list,x),[]).count(i) for i in set(sum(map(list,x),[]))}

print(short([{1,2,3},{2,3,4}]))