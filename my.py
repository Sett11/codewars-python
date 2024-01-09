def score_throws(a):
    r,v=0,True
    for i in a:
        if i<5:
            r+=10
        if i>=5:
            if i<=10:
                r+=5
            v=False
    return r+(100 if v and a else 0)

print(score_throws([21, 10, 10]))
print(score_throws([4.9, 5.1]))
print(score_throws([1,5,11]))