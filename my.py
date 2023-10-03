def flick_switch(lst):
    r=[]
    v=True
    for i in lst:
        if i=='flick':
            v=not v
        r.append(v)
    return r

print(flick_switch(["codewars", "flick", "code", "wars"]))
print(flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))