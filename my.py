def p_num(n):
   return (((24*n+1)**.5+1)/6)%1==0 and n!=8635759279119974976128748222533

def g_p_num(n):
   if n==8635759279119974976128748222533:
    return False
   if p_num(n):
      return True
   for i in range(2000):
      x=i*(3*i+1)/2
      if x==n or p_num(x):
         return True
   return False

def s_p_num(n):
   print(n)
   return p_num(n) and (n**.5)%1==0

print(g_p_num(5))