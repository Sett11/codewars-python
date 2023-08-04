def arrange(s):
    i,j,a,v=0,len(s)-1,[],True
    while i<=j:
        if i==j:
            a.append(s[i])
            break
        if v:
            a.append(s[i])
            a.append(s[j])
        else:
            a.append(s[j])
            a.append(s[i])
        v=not v
        i+=1
        j-=1
    return a

print(arrange([9, 7, -2, 8, 5, -3, 6, 5, 1]))
print(arrange([2, 4, 3, 4]))