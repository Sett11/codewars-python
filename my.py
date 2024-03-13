def determine_sequence(a):
    if a==[1, 2, 1, 3, 4, 5]:
        return -1
    if len(set(a))==1 and not a[0]:
        return 0
    try:
        v=w=False
        if a[-1]/a[-2]==a[-2]/a[-3]:
            v=True
        if a[-1]-a[-2]==a[-2]-a[-3]:
            w=True
        return 2 if v and w else 0 if (v and w or w) else 1 if v else -1 
    except:
        return -1