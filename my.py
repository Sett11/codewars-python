def get_matrix_product(a,b):
    if len(a[0])!=len(b):
        return
    n,m,l=len(a),len(b[0]),len(b)
    r=[[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(l):
                r[i][j]+=a[i][k]*b[k][j]
    
    return r
    
print(get_matrix_product([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(get_matrix_product([[0.5, 1],[1.5, 2]], [[0.2, 0.4], [0.6, 0.8]]))