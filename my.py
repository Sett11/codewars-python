def even_and_odd(n):
    n = list(map(int, list(str(n))))
    return tuple([int(''.join(list(map(str, filter(lambda e: e % 2 == 0, n)))) or 0), int(''.join(list(map(str, filter(lambda e: e % 2 != 0, n)))) or 0)])


print(even_and_odd(4628))
