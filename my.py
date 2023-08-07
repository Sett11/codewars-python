def like_or_dislike(l):
    a=[]
    for i in l:
        a.append(i)
        if len(a)==2:
            if a[0]==a[1]:
                a=[]
            else:
                a=a[-1:]
    return a[0] if a else 'Nothing'

print(like_or_dislike(['Like', 'Like', 'Dislike', 'Like', 'Like', 'Like', 'Like', 'Dislike']))
