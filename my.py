def largest_sum(a):
   m=n=0
   for i in a:
      n+=i
      if n<0:
         n=0
      if n>m:
         m=n
   return m

print(largest_sum([31,-41,59,26,-53,58,97,-93,-23,84]))