def operation(a,b,c=0):
  a,b=max(a,b),min(a,b)
  return c if a==b else operation((a-1)//2 if a&1 else a//2,b,c+1)

print(operation(9,2))
print(operation(1,4))