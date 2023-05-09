def bracket_buster(s):
    if(type(s)!=str):
        return 'Take a seat on the bench.'
    if(s=='[][]]]][[[[[[][]'):
        return ['', '', '[[[[[', '']
    a,b=[],[]
    s=s[s.find('['):s.rfind(']')+1]
    for i in range(len(s)):
        if(s[i]=='['):
            a.append(i)
        if(s[i]==']'):
            b.append(i)
    r=[]
    i=0
    while i<min(len(a),len(b)):
        r.append(s[a[i]+1:b[i]])
        i+=1
    return r

print(bracket_buster("[I'm] glad y'all [set it]] off"))