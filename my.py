def sequence_classifier(a):
    if a[0]==a[-1]:
        if len(a)>2:
            if a[1]==a[0]:
                return 5
            else:
                return 0
    r=sorted(a)
    if r==a:
        if len(set(a))==len(a):
            return 1
        else:
            return 2
    if r[::-1]==a:
        if len(set(a))==len(a):
            return 3
        else:
            return 4
    return 0
        

print(sequence_classifier([3,5,8,9,14,23]))