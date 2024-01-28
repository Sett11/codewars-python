def different_squares(a):
    n,m,s=len(a),len(a[0]),set()
    for i in range(n-1):
        for j in range(m-1):
            s.add(tuple((tuple(a[i][j:j+2]),tuple(a[i+1][j:j+2]))))
    return len(s)

print(different_squares([
          [1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]))