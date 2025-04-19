def get_sum(n):
    s1 = n * (n + 1) * (2 * n + 1) // 3
    s2 = 3 * n * (n + 1) // 2
    s3 = n + 1
    return s1 + s2 + s3

print(get_sum(3))