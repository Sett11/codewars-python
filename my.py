def word_wrap(s,l):
    a,r,t=s.split()[::-1],[],''
    while a:
        q=a.pop()
        n,k=len(t),len(q)
        if n==l:
            r.append(t.strip())
            t=''
        if n+k+1<=l:
            t=f'{t} {q}'.strip()
        else:
            if k>l:
                t,q=f'{t} {q[:l-n]}'.strip(),q[l-n:]
                if len(t)>l:
                    q=t[-1]+q
                    t=t[:-1]
                a.append(q)
            else:
                if t:
                    r.append(t)
                t=q
    return '\n'.join(r+[t])

print(word_wrap('areallylongword',6))
print(word_wrap("a lot of words for a single line",10))
print(word_wrap('greedy whenthewordistoolong', 7))