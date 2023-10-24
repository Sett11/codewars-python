def global_estimate(t):
    a=[sum(i) for i in zip(*t)]
    return a[0],sum(a)/2,a[1]

print(global_estimate(((1, 3), (1, 4), (1, 5))))