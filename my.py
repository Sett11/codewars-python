def any_odd(n):
    return '1' in bin(n)[2:][::-1][:32][1::2]

print(any_odd(128))
print(any_odd(9730854933))