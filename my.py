def last_digit(a):
    n=1
    for i in a[::-1]:
        n=i**(n if n<4 else n%4+4)
    return n%10

print(last_digit([123232, 694022, 140249]))