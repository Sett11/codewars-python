def swap_adjacent_bits(n):
    n=list(str(bin(n)))[slice(2,100)];i=0
    while len(n)%8!=0:
        n.insert(0,'0')
    while i<len(n)-1:
        n[i],n[i+1]=n[i+1],n[i]
        i+=2
    return int(''.join(n),2)

print(swap_adjacent_bits(83748))