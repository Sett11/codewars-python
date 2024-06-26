from itertools import combinations_with_replacement as c

def find_all(k,l):
    r=[int(''.join(map(str,i))) for i in c(list(range(1,10)),l) if sum(i)==k]
    return [len(r),r[0],r[-1]] if r else []

print(find_all(10,3))
print(find_all(84,4))
print(find_all(35,6))