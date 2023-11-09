def zebulans_nightmare(s):
    a=s.split('_')
    return ''.join(a[:1]+[i[0].upper()+i[1:] for i in a[1:]])

print(zebulans_nightmare('kkk_lll'))
print(zebulans_nightmare('hhh'))