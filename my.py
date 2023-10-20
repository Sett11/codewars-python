def generate_number(a,n):
    if n not in a:
        return n
    for i in range(1,10):
        for j in range(1,10):
            if i+j==n:
                t=int(str(i)+str(j))
                if t not in a:
                    return t

print(generate_number([1,2,3,4,6,9,10,11,15,29, 69], 11))