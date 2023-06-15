def kaprekar_split(n):
    s,i=str(n**2),1
    while i<len(s):
        if(int(s[:i])+int(s[i:])==n):
            return i
        i+=1
    return -1 if int(s)!=n else 0

print(kaprekar_split(9999999999))
print(kaprekar_split(2223))