def encode(s):
   c=''
   i=0
   j=i+1
   s+=str(0)
   while i<len(s):
      j=i+1
      while j<len(s):
         if(s[j]!=s[i]):
            c+=s[i:j][0]+str(len(s[i:j]))
            i=j-1
            break
         j+=1
      i+=1
   return c

print(encode("AAAALOTOOOOFTEEEEXXXXXXT"))