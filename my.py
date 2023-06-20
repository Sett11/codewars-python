def tap_code_translation(s):
    s=s.upper().replace('K','C')
    a=['ABCDE','FGHIJ','LMNOP','QRSTU','VWXYZ']
    r,i=[],0
    while i<len(s):
        j=0
        while j<len(a):
            if(s[i] in a[j]):
                r.append(''.join(['.'*(j+1)+' '+'.'*(a[j].index(s[i])+1)]))
            j+=1
        i+=1
    return ' '.join(r)

print(tap_code_translation('dot'))