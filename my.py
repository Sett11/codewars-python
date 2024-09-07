def solve(s):
   n,c=len(s),0
   for i in range(n):
      for j in range(i+1,n+1):
         if int(s[i:j])&1:
            c+=1
   return c

print(solve('13472315'))