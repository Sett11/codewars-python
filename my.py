def cart_prod(*a):
    l=len(a)
    if l==1:
        return {(i,) for i in a[0]}
    if l==2:
        return {(i,j) for i in a[0] for j in a[1]}
    if l==3:
        return {(i,j,k) for i in a[0] for j in a[1] for k in a[2]}
    if l==4:
        return {(i,j,k,b) for i in a[0] for j in a[1] for k in a[2] for b in a[3]}
    if l==5:
        return {(i,j,k,b,c) for i in a[0] for j in a[1] for k in a[2] for b in a[3] for c in a[4]}
    if l==6:
        return {(i,j,k,b,c,d) for i in a[0] for j in a[1] for k in a[2] for b in a[3] for c in a[4] for d in a[5]}
    if l==7:
        return {(i,j,k,b,c,d,e) for i in a[0] for j in a[1] for k in a[2] for b in a[3] for c in a[4] for d in a[5] for e in a[6]}
    if l==8:
        return {(i,j,k,b,c,d,e,f) for i in a[0] for j in a[1] for k in a[2] for b in a[3] for c in a[4] for d in a[5] for e in a[6] for f in a[7]}
    if l==9:
        return {(i,j,k,b,c,d,e,f,q) for i in a[0] for j in a[1] for k in a[2] for b in a[3] for c in a[4] for d in a[5] for e in a[6] for f in a[7] for q in a[8]}
    if l==10:
        return {(i,j,k,b,c,d,e,f,q,w) for i in a[0] for j in a[1] for k in a[2] for b in a[3] for c in a[4] for d in a[5] for e in a[6] for f in a[7] for q in a[8] for w in a[9]}
    return {()}

print(cart_prod({1}))
print(cart_prod({1, 2},{1, 2, 3}))
print(cart_prod({1},{1, 2},{1, 2, 3}))