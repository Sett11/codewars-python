def elections_winners(a,k):
  m=max(a)
  return len([i+k for i in a if i+k>m]) if k else 1 if a.count(m)==1 else 0

print(elections_winners([2,3,2,5],3))