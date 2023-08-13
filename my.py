def lazy(n):
    def d(f):
       def c(*a,**b):
          if n>0:
             if d.c==n:
                s=f(*a,**b)
             else:
                s=None
             d.c-=1
          if n<0:
             if d.c+1==0:
                s=None
             else:
                s=f(*a,**b)
             d.c+=1
          if d.c==0:
             d.c=n
          return s
       d.c=n
       return c
    return d

@lazy(4)
def half(x):
  return x/2

print(half(10))
print(half(10))
print(half(10))
print(half(10))