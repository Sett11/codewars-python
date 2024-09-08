def build_or_buy(s):
   r=[]
   if all(i in s for i in 'bw'):
      r.append('road')
   if all(i in s for i in 'bwsg'):
      r.append('settlement')
   if all(i in s for i in 'ooogg'):
      if s.count('o')>=3 and s.count('g')>=2:
         r.append('city')
   if all(i in s for i in 'osg'):
      r.append('development')
   return r

print(build_or_buy('bwsg'))