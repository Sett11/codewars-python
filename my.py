def brain_luck(s,c):
   db,res=[0],[]
   i=j=k=0
   while i<len(s):
      if s[i]=='>':
         if j==len(db)-1:
            db.append(0)
         j+=1
      elif s[i]=='<':
         if j==0:
            db.insert(0,0)
         else:
            j-=1
      elif s[i]=='+':
         db[j]+=1
         if db[j]==256:
            db[j]=0
      elif s[i]=='-':
         db[j]-=1
         if db[j]==-1:
            db[j]=255
      elif s[i]=='.':
         res.append(chr(db[j]))
      elif s[i]==',':
         db[j]=ord(c[k])
         k+=1
      elif s[i]=='[':
         if db[j]==0:
            x=1
            while x:
               i+=1
               if s[i]=='[':
                  x+=1
               elif s[i]==']':
                  x-=1
      elif s[i]==']':
         if db[j]:
            x=1
            while x:
               i-=1
               if s[i]==']':
                  x+=1
               elif s[i]=='[':
                  x-=1
      i+=1
   return ''.join(res)

print(brain_luck(',[.[-],]', 'Codewars' + chr(0)))