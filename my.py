def validate_ean(c):
    s=sum([int(i)*3 if j&1 else int(i) for j,i in enumerate(c[:-1])])
    return int(c[-1])==(0 if s%10==0 else 10-(s%10))

print(validate_ean('4003301018398'))
print(validate_ean('9783827317100'))