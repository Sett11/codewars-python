def spoonerize(s):
    a=[list(i) for i in s.split(' ')]
    a[0][0],a[1][0]=a[1][0],a[0][0]
    return ' '.join([''.join(i) for i in a])