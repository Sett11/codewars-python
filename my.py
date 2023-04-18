def match(a,b,c):
    one=list('.'.join(list(map(lambda e:'0'*(8-len(bin(int(e))[2:]))+bin(int(e))[2:],a.split('.')))))
    two=list('.'.join(list(map(lambda e:'0'*(8-len(bin(int(e))[2:]))+bin(int(e))[2:],b.split('.')))))
    three=list('.'.join(list(map(lambda e:'0'*(8-len(bin(int(e))[2:]))+bin(int(e))[2:],c.split('.')))))
    i=0
    while i<len(one):
        if(two[i]=='0' and one[i]!=three[i]):return False
        i+=1
    return True

print(match("192.168.0.0", "0.0.0.255",   "192.168.0.1"))
print(match('192.168.0.1', '0.0.0.0', '192.168.0.1'))