def smallest_transform(n):
    l=[int(i) for i in (str(n))]
    return min([[sum([abs(i-j) for j in l])][0] for i in l])

print(smallest_transform(1234))
print(smallest_transform(589))
print(smallest_transform(666))
print(smallest_transform(10932))