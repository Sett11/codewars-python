def pass_the_bill(a,b,c):
    return -1 if c*2>=a else 0 if b*2>a else a//2+1-b

print(pass_the_bill(16,8,7))