def comes_after(s,l):
    s+='0'
    return ''.join(filter(lambda e:e.isalpha(),[s[i+1] for i in range(len(s)-1) if s[i].lower()==l.lower()]))


print(comes_after("Pirates say arrrrrrrrr.", 'r'))