def max_and_min(a,b):
    a,b=sorted(a),sorted(b)
    m,u,n=max(abs(a[-1]-b[0]),abs(b[-1]-a[0])),set(b),min(abs(a[0]-b[0]),abs(a[-1]-b[-1]),abs(a[-1]-b[0]),abs(b[-1]-a[0]))
    for i in a:
        for j in range(20):
            if i-j in u or i+j in u:
                n=min(j,n)
                if not n:
                    return m,n
    return m,n

print(max_and_min([-870,91,-141,-739,707,-803,-195,-963,99,861],[796,-468,889,58,-765,-901,-311,-399,-764,-181,841,-670,-589]))