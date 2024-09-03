def find_squares(n,m):
   return m*(m+1)*(2*m+1)//6+(n-m)*m*(m+1)//2

print(find_squares(11,4))