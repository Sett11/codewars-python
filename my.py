def growing_plant(u,d,h):
    if(u>=h):return 1
    i=u;c=1
    while i<h:
        i+=u-d;c+=1
    return c

print(growing_plant(100,10,910))