def boolfuck(s,c=''):
   c=list(map(int,''.join(bin(ord(i))[2:][::-1].ljust(8,'0') for i in c)))
   while len(c)%8:
      c+=[0]
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
         db[j]=0 if db[j]==1 else 1
      elif s[i]==',':
         db[j]=c[k] if k<len(c) else 0
         k+=1
      elif s[i]==';':
         res.append(db[j])
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
   while len(res)%8:
      res.append(0)
   return ''.join(chr(int(''.join(str(j) for j in res[i:i+8][::-1]),2)) for i in range(0,len(res),8))

print(boolfuck('>,>,>,>,>,>,>,>,<<<<<<<<>;>;>;>;>;>;>;>;<<<<<<<<','*'))
print(boolfuck(";;;+;+;;+;+;+;+;+;+;;+;;+;;;+;;+;+;;+;;;+;;+;+;;+;+;;;;+;+;;+;;;+;;+;+;+;;;;;;;+;+;;+;;;+;+;;;+;+;;;;+;+;;+;;+;+;;+;;;+;;;+;;+;+;;+;;;+;+;;+;;+;+;+;;;;+;+;;;+;+;+;", ""))
print(boolfuck(">,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<;>;>;>;>;>;>;>;<<<<<<<,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]", "Codewars\u00ff"))