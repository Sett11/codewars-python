import re
def i_or_f(s):
    if(' ' in s or '+-' in s or '-+' in s or '++' in s or '--' in s or 'e-' in s):
        return False
    return True if re.sub(r'[^a-z]','',s.lower())=='e' or re.sub(r'[^a-z]','',s.lower())=='' and len(re.sub(r'[^\.]','',s) )<2 else False

print(i_or_f('1'))