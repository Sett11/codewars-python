from re import sub

def dad_filter(s):
    return sub(r',$|\s^','',sub(r',+',',',s.strip()))

print(dad_filter("Dead or alive,,,, you're coming with me,,,   "))