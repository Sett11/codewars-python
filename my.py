import re

def to24hourtime(h,m,p):
    s=('0' if h<10 and p!='pm' else '')+f'{h+(12 if p=="pm" and h<12 else 0)}{("0" if m<10 else "")+str(m)}'
    return s if p=='pm' else re.sub(r'^12','00',s)

print(to24hourtime(1,0,'am'))
print(to24hourtime(9,45,'pm'))
print(to24hourtime(12,0,'am'))
print(to24hourtime(12,0,'pm'))