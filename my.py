get_evil=lambda n:(k:=2*n-1,2*(n-1))[len(bin(k)[2:].replace('0',''))&1]

print(get_evil(2))