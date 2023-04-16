def motif_locator(s,c,i=0):
    r=[]
    while i<len(s)-len(c)-1:
        r.append(s.find(c,i)+1)
        i+=1
    return list(filter(lambda e:e,sorted(list(set(r)))))

print(motif_locator("ACGTTACAACGTTAG", "ACGT"))