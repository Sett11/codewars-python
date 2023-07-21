def get_section_id(s,c):
    x=0
    for i in range(len(c)):
        x+=c[i]
        if c[i]>s:
            return i
        if c[i]==s:
            return i+1
        if s<x:
            return i
    return -1

print(get_section_id(299, [300, 200, 400, 600, 100]))
print(get_section_id(300, [300, 200, 400, 600, 100]))