import numpy as np

def check(x):
    if isinstance(x, (int, float)):
        x = np.array([x])
    n = (np.sqrt(8 * x + 1) - 1) / 2
    return n == np.floor(n)

def search_start(x):
    while x % 3 != 0:
        x+=1
    return x

def same_col_seq(n, k, col):
    nums = {'blue': 0, 'red': 1, 'yellow': 2}
    s = search_start(n+1) + nums[col]
    a = np.arange(s, 2 * k * n + 4, 3)
    mask = check(a)
    return [int(i) for i in a[mask][:k]]
    

print(same_col_seq(3, 3, 'blue'))
print(same_col_seq(250, 6, 'yellow'))
print(same_col_seq(17076, 20, 'blue'))