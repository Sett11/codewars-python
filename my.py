from statistics import mean
def distances_from_average(a):
    s=mean(a)
    return [round(s-i,2) for i in a]

print(distances_from_average([55, 95, 62, 36, 48]))