from re import sub,IGNORECASE

def vowel_start(s): 
    a=sub(r'[aioue]',lambda e:' '+e.group(),sub(r'\W','',s.lower().replace('_','')),flags=IGNORECASE).split(' ')
    i=1
    while i<len(a):
        if len(a[i])==1 and a[i] not in 'aioue':
            a[i-1]+=a.pop(i)
            i-=1
        i+=1
    return ' '.join(a).strip()


print(vowel_start('It is beautiful we---ather today!'))
print(vowel_start('my number is 0208-533-2325'))
print(vowel_start('under_score'))