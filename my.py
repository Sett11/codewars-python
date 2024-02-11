def get_password(a,b):
    n,m,r=len(a),len(a[0]),''
    k=p=0
    v=False
    for i in range(n):
        if v:
            break
        for j in range(m):
            if a[i][j]=='x':
                k=i
                p=j
                v=True
                break
    for i in b:
        t=i.replace('T','')
        if t=='left':
            p-=1
        if t=='right':
            p+=1
        if t=='up':
            k-=1
        if t=='down':
            k+=1
        if i.endswith('T'):
            r+=a[k][p]
    return r

print(get_password([
            ["x", "l", "m"],
            ["o", "f", "c"],
            ["k", "i", "t"]
          ],["rightT", "down", "leftT", "right", "rightT", "down", "left", "leftT"]))