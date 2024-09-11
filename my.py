def variance(a):
    u=[len(i) for i in a]
    n=len(u)
    m=sum(i*(1/n) for i in u)
    return round(sum(1/n*(i-m)**2 for i in u),4)

print(variance(['Hi','World']))
print(variance(['The', 'girl', 'put', 'on', 'her', 'beautiful', 'red', 'hat']))