import re
def sursurungal(s):
    s,a,i=re.split(r'(\W+)',s),[],0
    while i<len(s):
        if(s[i].isdigit()):
            n=int(s[i])
            if n<2:
                a.append(f'{s[i]} {s[i+2]}')
            else:
                t=s[i+2]
                t=t[:-1]
                if n==2:
                    a.append(f'{s[i]} bu{t}')
                if 3<=n<=9:
                    a.append(f'{s[i]} {t}zo')
                if n>=10:
                    a.append(f'{s[i]} ga{t}ga')
            i+=3
        else:
            a.append(s[i])
            i+=1
    return ''.join(a)


print(sursurungal("""3 pigs
met 1 wolf
2 days ago"""))
print(sursurungal("3 bananas"))