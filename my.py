def solve(arr):
    n,a=1,sorted(arr)
    for i in a:
        if i<=n:
            n+=i
        else:
            break
    return n