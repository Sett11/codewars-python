import re as r

def encode(s):
   c=''
   i=0
   j=i+1
   s+=str(0)
   while i<len(s):
      j=i+1
      while j<len(s):
         if(s[j]!=s[i]):
            c+=str(len(s[i:j]))+s[i:j][0]
            i=j-1
            break
         j+=1
      i+=1
   return c

def decode(s):
   c=''
   w=r.sub(r'\d+',lambda e:' '+e.group()+' ',s).split()
   i=0
   a=[]
   while i<len(w):
      a.append(w[slice(i,i+2)])
      i+=2
   i=0
   while i<len(a):
      c+=a[i][1]*int(a[i][0])
      i+=1
   return c

print(decode("10A1B"))
#print(encode (decode ("10A1B")))