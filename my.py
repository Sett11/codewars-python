def score(n):
    return int(bin(n)[2:].replace('0','1'),2) if n>0 else 0

print(score(923056238))
print(score(49))