def x_marks_the_spot(a):
    r=[]
    for i,j in enumerate(a):
        for k,p in enumerate(j):
            if p=='x':
                r.append([i,k])
    return r[0] if r and len(r)==1 else []

print(x_marks_the_spot([
          ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
          ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
          ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
          ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
          ['o', 'o', 'o', 'o', 'o', 'o', 'x', 'o'],
          ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
        ]))