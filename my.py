def reverse_it(d):
    if(type(d)==str):
        return d[::-1]
    if(type(d)==int):
        return int(str(d)[::-1])
    if(type(d)==float):
        return float(str(d)[::-1])
    return d

print(reverse_it('Hello'))
print(reverse_it(1234))
print(reverse_it('h2buua6b0z2b6'))