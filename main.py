def micro_world(a, k):
    a.sort()
    i, w = 0, True
    while w:
        w = False
        for i in range(len(a)-1):
            if a[i] < a[i+1] and a[i+1] <= a[i] + k:
                w = True
                a.pop(i)
                break
    return len(a)

print(micro_world([101, 53, 42, 102, 101, 55, 54], 1))
print(micro_world([20, 15, 10, 15, 20, 25], 5))