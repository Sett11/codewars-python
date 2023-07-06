def flip(d,a):
    a.sort()
    return a if d=='R' else a[::-1]

print(flip('R',[3, 2, 1, 2]))