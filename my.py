def args_to_string(a):
    s=''
    for i in a:
        if type(i)==str:
            s+='&'+i+'&'
        if type(i)==list:
            if len(i)==1:
                s+='&'+i[0]+'&'
            if len(i)==2:
                if len(i[0])>1:
                    s+='&--'+'&'.join(i)+'&'
                else:
                    s+='&-'+'&'.join(i)+'&'
    return s.replace('&&','&').replace('&',' ').strip()

print(args_to_string(['bar']))
print(args_to_string([["foo", "bar"], "baz"]))
print(args_to_string([["foo", "bar"], ["fack", "baz"]]))
print(args_to_string([["foo"], ["bar", "baz"], "qux"]))
print(args_to_string([["foo", "bar"], ["baz", "qux"]]))