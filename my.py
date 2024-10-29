def find_missing_number(a):
    m=max(a,default=1)
    try:
        return (set(range(1,m+1))^set(a)).pop()
    except:
        return m+1

print(find_missing_number([1,2,4]))