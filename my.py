def close_to_zero(t):
    s=t.split(' ')
    m=min([abs(0-int(i)) for i in s]) if t else 0
    return m if str(m) in s else -m if t else 0

print(close_to_zero('-37 4 -1 -42 -5 -43 28 20 8 2 -14 -30 42 -10 9 20 14 -23 -25 36 -48 2 19 -24 37 33 50 -18 29 -3 -28 7 -40 4 -11 -34 6 -22 -26 -12 47 -49'))
print(close_to_zero('28 35 -21 17 38 -17'))
print(close_to_zero('-1 50 -4 20 22 -7 0 10 -8'))