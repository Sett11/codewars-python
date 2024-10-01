def peak_and_valley(a):
    return [a[i] for i in range(3,len(a)-3) if all(a[i]>j for j in a[i-3:i]+a[i+1:i+4]) or all(a[i]<j for j in a[i-3:i]+a[i+1:i+4])]

print(peak_and_valley([10,20,30,40,30,20,10,11,12,13,14,15,16,15,14,13]))