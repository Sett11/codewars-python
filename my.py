def switch_endian(n,b):
    if (n).bit_length()>b or (b&(b-1)) or n<0:
        return
    s=bin(n)[2:].rjust(b,'0')
    return int(''.join([s[i:i+8] for i in range(0,b,8)][::-1]),2)

print(switch_endian(7206089, 32))