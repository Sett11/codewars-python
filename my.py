def encrypt(w,n):
    w=list(map(lambda e: ord(e)-96,w))
    while n>0:
        w=list(map(lambda e: e*3-5,w))
        n-=1
    return w

def decrypt(w,n):
    while n>0:
        w=list(map(lambda e: int((e+5)/3),w))
        n-=1
    return ''.join(list(map(lambda e: chr(e+96),w)))


print(decrypt([3, 9, 16, 8, 5, 18], -39245382957))