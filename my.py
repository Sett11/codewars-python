def shuffled_array(a):
    s=sum(a)
    for i in range(len(a)):
        if a[i]==s-a[i]:
            a.remove(a[i])
            return sorted(a)


print(shuffled_array([1, 12, 3, 6, 2]))