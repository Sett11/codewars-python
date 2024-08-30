from math import floor,sqrt

def poohbear(s):
   cache,res,db=[],[],[0]
   i=j=0
   while i<len(s):
      if s[i]=='+':
         db[j]+=1
         if db[j]==256:
            db[j]=0
      elif s[i]=='-':
         db[j]-=1
         if db[j]==-1:
            db[j]=255
      elif s[i]=='>':
         if j==len(db)-1:
            db.append(0)
         j+=1
      elif s[i]=='<':
         if j==0:
            db.insert(0,0)
         else:
            j-=1
      elif s[i]=='c':
         cache.append(db[j])
      elif s[i]=='p':
         db[j]=cache[-1]
      elif s[i]=='W':
         if db[j]:
            pass
         else:
            k=i
            while s[k]!='E':
               k+=1
            i=k
      elif s[i]=='E':
         if db[j]:
            k=i
            while s[k]!='W':
               k-=1
            i=k-1
         else:
            pass
      elif s[i]=='P':
         res.append(chr(floor(db[j])))
      elif s[i]=='N':
         res.append(str(floor(db[j])))
      elif s[i]=='T':
         db[j]*=2
      elif s[i]=='Q':
         db[j]=floor(db[j]**2)
      elif s[i]=='U':
         db[j]=floor(sqrt(db[j]))
      elif s[i]=='L':
         db[j]+=2
      elif s[i]=='I':
         db[j]-=2
      elif s[i]=='V':
         db[j]//=2
      elif s[i]=='A':
         db[j]+=cache[-1]
      elif s[i]=='B':
         db[j]-=cache[-1]
      elif s[i]=='Y':
         db[j]*=cache[-1]
      elif s[i]=='D':
         db[j]//=cache[-1]
      i+=1
   return ''.join(res)

         

print(poohbear('LQTcQAP>pQBBTAI-PA-PPL+P<BVPAL+T+P>PL+PBLPBP<DLLLT+P'))
print(poohbear('LQQT+P+P+P+P+P+P'))
print(poohbear('+c BANANA'))
print(poohbear('+LTQII>+WN<P>+E'))
print(poohbear('LILcABNBpYDYYYYLLL+P-+W-EQNW-ELLQUTTTT+P'))