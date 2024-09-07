def to_pretty(n):
   if n==0:
      return 'just now'
   if n<60:
      return f"{n if n>1 else ''}{'a' if n==1 else ''} second{'s' if n>1 else ''} ago"
   if n<3600:
      n//=60
      return f"{n if n>1 else ''}{'a' if n==1 else ''} minute{'s' if n>1 else ''} ago"
   if n<86400:
      n//=3600
      return f"{n if n>1 else ''}{'an' if n==1 else ''} hour{'s' if n>1 else ''} ago"
   if n<604800:
      n//=86400
      return f"{n if n>1 else ''}{'a' if n==1 else ''} day{'s' if n>1 else ''} ago"
   n//=604800
   return f"{n if n>1 else ''}{'a' if n==1 else ''} week{'s' if n>1 else ''} ago"
   

print(to_pretty(2220000))