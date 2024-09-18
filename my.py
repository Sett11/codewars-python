from statistics import mean

def variance(a):
    m=mean(a)
    return sum((i-m)**2 for i in a)/len(a)
    

print(variance([1.5, 2.5, 4, 2, 1, 1]))
print(variance([8, 9, 10, 11, 12]))
print(variance([-10, 0, 10, 20, 30]))