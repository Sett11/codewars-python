lowest_temp=lambda t:None if not t else min([int(i) for i in t.split(' ')])

print(lowest_temp('-1 50 -4 20 22 -7 0 10 -8'))