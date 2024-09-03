def sq_in_rect(l,w):
   r=[]
   while l and w:
      r.append(min(l,w))
      if l>w:
         l-=w
      else:
         w-=l
   return r if len(r)>1 else None

print(sq_in_rect(20,14))