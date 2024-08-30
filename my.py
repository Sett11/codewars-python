def underload(s):
   stack,res,i=[],[],0
   s=list(s)
   while i<len(s):
      if s[i]==')':
         raise Exception()
      elif s[i]=='(':
         j,k,r=i+1,1,''
         while k:
            if k<0 or j>=len(s):
               raise Exception()
            if s[j]=='(':
               k+=1
            elif s[j]==')':
               k-=1
            j+=1
         r+=''.join(s[i+1:j-1])
         i=j-1
         stack.append(r)
      elif s[i]==':':
         stack.append(stack[-1])
      elif s[i]=='!':
         stack.pop()
      elif s[i]=='~':
         x,y=stack.pop(),stack.pop()
         stack.extend([x,y])
      elif s[i]=='*':
         x=stack.pop()
         stack[-1]+=x
      elif s[i]=='a':
         stack[-1]=f'({stack[-1]})'
      elif s[i]=='^':
         s=s[:i]+list(stack.pop())+s[i+1:]
         i-=1
      elif s[i]=='S':
         res.append(stack.pop())
      i+=1
   return ''.join(res)
                

# print(underload("(hello):SS"))
# print(underload("(first)(second)~SS"))
print(underload("((aa)S)::**^"))