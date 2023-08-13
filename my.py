def digits_product(n):
    if n<10:
        return n+10
    s=''
    for i in range(9,1,-1):
        while not n%i:
            s+=str(i)
            n//=i
    return int(s[::-1]) if n==1 else -1

print(digits_product(450))