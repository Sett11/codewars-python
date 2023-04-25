from functools import reduce as r

def geometric_meanI(a):
     l=len(a)
     x=list(filter(lambda e:type(e)==str or e<0,a))
     if(l>=2 and l<=10 and len(x)>1 or l>10 and len(x)>l/10):
          return 0
     y=list(filter(lambda e:type(e)==int and e>=0,a))
     return pow(r(lambda a,c: a*c,y,1),1/len(y))

print(geometric_meanI([2, 2, 3, 0, 4, 10, -4, 8, 1, 4, 6, 7, 2]))