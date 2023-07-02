def stringy(s):
    return ''.join(['10'[i%2] for i in range(s)])

print(stringy(6))