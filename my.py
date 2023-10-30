def first_reverse_try(a):
    if len(a)<2:
        return a
    a[0],a[-1]=a[-1],a[0]
    return a