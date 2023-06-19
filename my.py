def archers_ready(h):
    return h==[i for i in h if i>4] if len(h) else False

print(archers_ready([1,2,3,8,9,10]))
print(archers_ready([8,9,10]))