def happy_g(s):
    return all(['gg' in s[i-1:i+2] for i in range(len(s)) if s[i]=='g' and s[i-1:i+2]])


print(happy_g('gg0gg3gg0gg'))
print(happy_g('gog'))