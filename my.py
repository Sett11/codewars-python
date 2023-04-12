import re
def range_bit_count(a,b):
    return len(re.sub(r'[^1]','',''.join(list(map(bin,list(range(a,b+1)))))))

print(range_bit_count(2,7))