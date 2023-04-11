def index_finder(a,x):
    i=1
    while i<len(a):
        if(a[i]==x):return i
        i+=1

print(index_finder(['b','a','b'], 'b'))