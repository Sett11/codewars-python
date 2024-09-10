from re import findall

def baum_sweet():
    i=0
    yield 1
    while True:
        i+=1
        k=1 if not [j for j in findall(r'0+',bin(i)[2:]) if len(j)&1] else 0
        yield k

gen=baum_sweet()

print([next(gen) for _ in range(20)])