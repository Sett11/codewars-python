from re import sub,IGNORECASE

def short_form(s):
    return s[0]+sub(r'[aouie]','',s[1:-1],flags=IGNORECASE)+s[-1]

print(short_form('assault'))