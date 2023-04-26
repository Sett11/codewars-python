def run_length_encoding(s):
   c=[]
   i=0
   j=i+1
   s+=str(0)
   while i<len(s):
      j=i+1
      while j<len(s):
         if(s[j]!=s[i]):
            c.append([len(s[i:j]),s[i:j][0]])
            i=j-1
            break
         j+=1
      i+=1
   return c

print(run_length_encoding("hello world!"))