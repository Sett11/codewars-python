def f(x):
    return len(x)==2 and x.isdigit()

def validate(s):
    s=s.split(' ')
    try:
        return s[0]=='MDZHB' and f(s[1]) and len(s[2])==3 and s[2].isdigit() and s[3].isalpha() and all([f(s[4]),f(s[5]),f(s[6]),f(s[7])])
    except:
        return False

print(validate('MDZHB 85 596 KLASA 81 00 02 91'))
print(validate('MDZHV 60 130 VATRUKH 58 89 54 54'))