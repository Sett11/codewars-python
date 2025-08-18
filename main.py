def count_sum_of_two_representations(n, l, r):
    k = t = n // 2
    if n % 2 != 0:
        t += 1
    c = 0
    while True:
        if k >= l and t <= r and k <= t:
            c += 1
        else:
            break
        k -= 1
        t += 1
    return c

print(count_sum_of_two_representations(93,24,58))