def next_smaller_pronic(n):
   k=int(n**.5)
   x=k*(k+1)
   return x if x<n else k*(k-1)

print(next_smaller_pronic(978845376))