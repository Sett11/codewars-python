def box_blur(a):
   n,m,r=len(a),len(a[0]),[]
   for i in range(1,n-1):
      r.append([])
      for j in range(1,m-1):
         t=0
         for k in range(i-1,i+2):
            for c in range(j-1,j+2):
               t+=a[k][c]
         r[i-1].append(t//9)
   return r

print(box_blur([
            [1, 1, 1],
            [1, 7, 1],
            [1, 1, 1]
        ]))
print(box_blur([
            [7, 4, 0, 1],
            [5, 6, 2, 2],
            [6, 10, 7, 8],
            [1, 4, 2, 0]
        ]))