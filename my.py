def digit_sum(n):
    return sum(map(int,list(str(n))))

print(digit_sum(4294967295))