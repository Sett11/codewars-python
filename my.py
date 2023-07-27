def cube_times(t):
    return round(sum(sorted(t)[1:-1])/3,2),min(t)

print(cube_times([9.5, 7.6, 11.4, 10.5, 8.1]))