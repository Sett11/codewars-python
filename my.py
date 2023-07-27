def valid_braces(s):
   if s.count('(')!=s.count(')') or s.count('[')!=s.count(']') or s.count('{')!=s.count('}') or '(]' in s:
     return False
   i,a=0,[]
   while i<len(s):
    if s[i]=='(':
      a.append(1)
    if s[i]==')':
      if 1 not in a:
        return False
      a[a.index(1)]=0
    if s[i]=='{':
      a.append(3)
    if s[i]=='}':
      if 3 not in a:
        return False
      a[a.index(3)]=0
    if s[i]=='[':
      a.append(5)
    if s[i]==']':
      if 5 not in a:
        return False
      a[a.index(5)]=0
    i+=1
   return True


print(valid_braces('{}()[]'))
print(valid_braces("([}{])"))
print(valid_braces("(({{[[]]}}))"))
print(valid_braces("{}({})[]"))