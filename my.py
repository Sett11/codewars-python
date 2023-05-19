def T9(w,s):
    o={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    i=0
    while i<len(s):
        w=[j for j in w if j[i].lower() in o[s[i]]]
        i+=1
    return w if len(w) else [''.join([o[i][0] for i in s])]

print(T9(['hello','world'],'43556'))
print(T9(['qveqa'],'43556'))