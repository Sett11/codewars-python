def rev_sub(a):
    i=0
    a.append('&')
    while i<len(a)-1:
        j=i
        if a[i]%2==0:
            while j<len(a):
                if a[j]=='&' or a[j]%2:
                    a=a[:i]+a[i:j][::-1]+a[j:]
                    i=j
                    break
                j+=1
        i+=1
    return a[:-1]

print(rev_sub([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(rev_sub([2, 4, 3, 10, 2]))