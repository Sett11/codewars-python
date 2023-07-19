def content_weight(w,s): 
    n=int(''.join([i for i in list(s) if i.isdigit()]))
    q=w//(n+1)*n
    return q if 'larger' in s.split(' ') else w-q

print(content_weight(500,"9 times larger"))
print(content_weight(1000, "999 times larger"))
print(content_weight(120, "2 times larger"))
print(content_weight(120, "2 times smaller"))