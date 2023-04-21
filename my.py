import re
def textin(s):
    return re.sub(r'too|two|to','2',s,flags=re.IGNORECASE)

print(textin('TwO ToO tWo tOo'))