from collections import Counter

def buy_fruits(a, b):
    c = sorted(Counter(b).values(), reverse=True)
    mn = mx = k = 0
    x, y = sorted(a), sorted(a,reverse=True)
    for i in c:
        mn += x[k] * i
        mx += y[k] * i
        k += 1
    return mn, mx

print(buy_fruits([3,5,1,6,8,1],["peach","grapefruit","banana","orange","orange"]))