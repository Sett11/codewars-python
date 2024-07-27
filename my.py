def convert_bits(a,b):
    return sum(i!=j for i,j in zip(bin(a)[2:].rjust(32,'0'),bin(b)[2:].rjust(32,'0')))

print(convert_bits(64809,706))