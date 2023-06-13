def seqlist(f,c,l):
    return [i for i in range(f,l*c*2,c)][:l]

print(seqlist(0,2,20))