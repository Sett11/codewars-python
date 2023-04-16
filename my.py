def fist_beard(a,i=0):
    r=[]
    while i<len(a):
        r.extend(list(map(chr,a[i])))
        i+=1
    return ''.join(r)

print(fist_beard([[78], [117, 110, 99], [104, 117], [107, 115]]))