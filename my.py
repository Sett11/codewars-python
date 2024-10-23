def subsets_parity(n,k):
    return ('ODD','EVEN')[bool(k&(n-k))]

print(subsets_parity(93,16))
print(subsets_parity(1,1))
print(subsets_parity(20,10))
print(subsets_parity(48,12))