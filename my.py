def smile(t):
    s,i=list(t+'..'),0
    while i<len(s)-2:
        if (s[i]==':' or s[i]==';' or s[i]=='=') and (s[i+1]=='-' or s[i+1]=='~') and (s[i+2]=='(' or s[i+2]=='['):
            s[i+2]=')' if s[i+2]=='(' else ']'
        elif (s[i]==':' or s[i]==';' or s[i]=='=') and (s[i+1]=='(' or s[i+1]=='['):
            s[i+1]=')' if s[i+1]=='(' else ']'
        i+=1
    return ''.join(s)[:-2]

print(smile('Howdy :('))
print(smile('Never be sad =['))
print(smile('It\'s been raining all day ;-('))
print(smile('Change this `=(` and this `:[`'))
print(smile('The list of positive numbers is [1,2,3,4...]'))
print(smile('(((-)(((-)))(-)))'))