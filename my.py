def perimeter(n):
   a=b=c=1
   while n:
      c+=b
      a,b=b,a+b
      n-=1
   return c*4

print(perimeter(500))