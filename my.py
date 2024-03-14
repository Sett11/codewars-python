def corner_fill(a):
    r,v=[],1
    while a:
        q=a.pop(0)
        for i in range(len(a)):
            q.append(a[i].pop())
        r.extend(q if v&1 else q[::-1])
        v+=1
    return r

print(corner_fill([
  [4,  1, 10,  5],
  [7,  8,  2, 16],
  [15, 14, 3,  6],
  [11, 9, 13, 12]
]))