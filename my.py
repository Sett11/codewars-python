def sort_transform(a):
    r=sorted(a)
    q=r[::-1]
    w=sorted(a,key=chr)
    return f"{''.join(map(chr,a[:2]+a[-2:]))}-{''.join(map(chr,r[:2]+r[-2:]))}-{''.join(map(chr,q[:2]+q[-2:]))}-{''.join(map(chr,w[:2]+w[-2:]))}"


print(sort_transform([111, 112, 113, 114, 115, 113, 114, 110]))