from re import sub

def spin_solve(s):
    a=s.split(' ')
    for i in range(len(a)):
        t=len(sub(r'[^A-z]','',a[i]))
        if t==1:
            a[i]='0'
        elif t==2 or (',' in a[i] and t<7):
            a[i]=a[i].upper()
        elif t>6 or a[i].lower().count('t')==2:
            if not a[i][-1].isalpha():
                a[i]=a[i][:-1][::-1]+a[i][-1]
            else:
                a[i]=a[i][::-1]
    return ' '.join(a)

print(spin_solve("If a man does not keep pace with his companions, perhaps it is because he hears a different drummer."))