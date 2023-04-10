def fix_the_meerkat(a):
    b=a[0]
    c=a[2]
    a[0]=c
    a[2]=b
    return a
        

print(fix_the_meerkat(["tail", "body", "head"]))