def are_similar(a,b):
    if a==b:
        return True
    try:
        t,p=[i for i,j in enumerate(a) if a[i]!=b[i]]
        b[t],b[p]=b[p],b[t]
        return a==b
    except:
        return False

print(are_similar([1, 2, 3],[2, 1, 3]))