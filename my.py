def f(a,b):
    return True if a==b or not b else False if int(a)>int(b) or a not in b or b.index(a)!=0 else f(str(int(a)+1),b[len(a):])

def find(s):
    i=1
    while i<len(s):
        t,p=str(int(s[:i])+1),s[i:]
        if f(t,p):
            return int(t)-1
        i+=1
    return int(s)

print(find('123456789101112131415'))
print(find('17181920'))
print(find('99100'))
print(find('127151127152127153127154127155127156127157'))
print(find('577495'))