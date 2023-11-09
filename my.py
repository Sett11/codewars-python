def magic_sum(a):
    return sum(filter(lambda e:e&1 and '3' in str(e),a))

print(magic_sum([3, 12, 5, 8, 30, 13]))