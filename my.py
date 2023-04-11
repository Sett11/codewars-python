def second_symbol(s,c):
    a=[]
    i=0
    while i<len(s):
        if(s[i]==c and len(a)!=0):
            return i
        if(s[i]==c and len(a)==0):
            a.append(1)
        i+=1
    return -1

print(second_symbol('Hello world!!!','A'))