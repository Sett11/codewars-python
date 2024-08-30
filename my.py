def interpreter(s):
   db,res,pos,i=[0],'',0,0
   while s[i]!='&':
      if s[i]=='<':
         if pos==0:
            db.insert(0,0)
         else:
            pos-=1
      elif s[i]=='>':
         if pos==len(db)-1:
            db.append(0)
         pos+=1
      elif s[i]=='+':
         db[pos]+=1
         if db[pos]==256:
            db[pos]=0
      elif s[i]=='-':
         db[pos]-=1
         if db[pos]==-1:
            db[pos]=255
      elif s[i]=='*':
         res+=chr(db[pos])
      elif s[i]=='/':
         if db[pos]==0:
            i+=1
      elif s[i]=='\\':
         if db[pos]:
            i+=1
      else:
         pass
      i+=1
      if i>=len(s):
         i%=len(s)
   return res

print(interpreter('+*\&'))