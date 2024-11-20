from preloaded import LOVE_LANGUAGES as l

def love_language(p,n):
    r={i:0 for i in l}
    for i in range(7*n):
        if p.response(l[i%5])=='positive':
            r[l[i%5]]+=1
    return max(r.items(),key=lambda x:x[1])[0]