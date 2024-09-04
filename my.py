def f(a):
   x=next(a)
   while 1:
      try:
         y=next(a)
         yield y.__sub__(x)
         x=y
      except StopIteration:
         return

def delta(v,n):
   a=iter(v)
   if n==0:
      return a
   return delta(f(a),n-1)