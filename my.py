def reverse_slice(s):
    return [s[::-1][i:] for i in range(len(s))]

print(reverse_slice('123'))