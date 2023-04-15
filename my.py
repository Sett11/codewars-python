def each_char(s,a):
    if(not s):return ''
    return a.join(list(s))+a if(isinstance(a,str)) else ''.join(list(map(a,list(s))))

print(each_char("hello",lambda c: c.upper()))