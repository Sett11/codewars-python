def count_targets(n,a):
    return len(list(filter(bool,[a[i]==a[i-n] for i in range(n,len(a))])))

print(count_targets(7,[72, 53, 91, 91, 89, 59, 49, 9, 98, 84, 18, 65, 61, 49, 20, 44, 84, 18, 68, 61, 31, 20, 1, 84, 20, 68, 92, 65, 20, 83, 52, 26, 94, 76, 63, 67, 83, 17, 12]))