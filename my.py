def kill_kth_bit(n,k):
    r=list(bin(n)[slice(2,100)])
    r.reverse()
    if(k>=len(r)):k%=len(r)
    r[k-1]='0'
    r.reverse()
    return int(''.join(r),2)

print(kill_kth_bit(2147483647,16))