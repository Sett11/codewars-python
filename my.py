def rotate(l,n):
    if(not n or not len(l)):
        return l
    n=n%len(l)
    if(n>0):
      while n:
         l.insert(0,l.pop())
         n-=1
    else:
       while n:
          l.append(l.pop(0))
          n+=1
    return l

print(rotate([1, 2, 3, 4, 5],12478))