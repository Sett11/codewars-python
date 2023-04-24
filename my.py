import re
def case_sensitive(s):
    r=re.sub(r'[a-z]','',s)
    return [False,[r]] if r else [True,[]]
    
print(case_sensitive('asd'))
print(case_sensitive('cellS'))