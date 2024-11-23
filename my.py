def assistance(w):
    if w<=25:
        return 'Only lock' if w==25 else "Nothing to hang" if w==20 else 'Error'
    plates,r={25: 'red', 20: 'blue', 15: 'yellow', 10: 'green', 5: 'black', 2.5: 'orange', 1.25: 'white'},[]
    w-=25
    for i in plates:
        if w>i and i*2<=w:
            k=0
            while w>i and i*2<=w:
                k+=1
                w-=i*2
            r.append(f'{k} {plates[i]}{"s" if k>1 else ""}')
    return ', '.join(r)+', lock' if w==0 else 'Error'

print(assistance(345))