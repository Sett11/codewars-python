def find_incorrect_value(a):
    a=[0]+a
    n,i=len(a),1
    while i*2+1<n:
        if a[i]!=a[i*2]+a[i*2+1]:
            x,y=i*2,i*2+1
            if x*2+1>=n:
                return x,a[i]-a[x]
            if y*2+1>=n:
                return y-1,a[i]-a[x]
            if a[x]!=a[x*2]+a[x*2+1]:
                return x-1,a[x*2]+a[x*2+1]
            if a[y]!=a[y*2]+a[y*2+1]:
                return y-1,a[y*2]+a[y*2+1]
            return i-1,a[x]+a[y]
        i+=1

print(find_incorrect_value( [29, 13, 16, 5, 8, 9, 1]))
print(find_incorrect_value( [27, 13, 15, 6, 7, 5, 9]))