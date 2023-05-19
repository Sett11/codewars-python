def simple_sum(a,b):
    return simple_sum(a^b,(a&b)<<1) if b else a

print(simple_sum(2,3))