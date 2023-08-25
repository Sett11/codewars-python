time_per_day=lambda l:round(round(sum([.75*i[0]*i[1] for i in l])/60/5*1000,1)/1000,2)

print(time_per_day([(1, 20), (2, 10), (3, 15), (4, 10)]))
print(time_per_day([(4, 11), (9, 42)]))
print(time_per_day([(9, 38)]))