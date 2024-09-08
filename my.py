from re import sub,search


def brainfuck_to_c(s):
   r=r'(\+\-)|(\-\+)|(\<\>)|(\>\<)|(\[\])'
   s=sub(r'[^\+\-\<\>\,\.\[\]]','',s)
   while search(r,s):
      s=sub(r,'',s)
   s=sub(r'(\+|\-)+',lambda x:f'*p {x.group()[0]}= {len(x.group())};\n',s)
   s=sub(r'(\<|\>)+',lambda x:f"p {'-' if x.group()[0]=='<' else '+'}= {len(x.group())};\n",s)
   res=sub(r'\.|\,|\[|\]',lambda x:{'.':'putchar(*p);\n',',':'*p = getchar();\n','[':'if (*p) do {\n',']':'} while (*p);\n'}[x.group()],s).splitlines()
   c=0
   for i in range(len(res)):
      if c<0:
         return 'Error!'
      res[i]=' '*c+res[i]
      if 'if' in res[i]:
         c+=2
      if 'while' in res[i]:
         c-=2
         res[i]=res[i][2:]
   return 'Error!' if c else '\n'.join(res)+('\n' if res else '')
      

print(brainfuck_to_c(("[>>[<<]]")))