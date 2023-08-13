def averages(a):
    return [] if not a else [(a[i]+a[i+1])/2 for i in range(len(a)-1)]

print(averages([ 1, 3, 5, 1, -10]))