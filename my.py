import re
def remove_char(l):
    return ['$'+j[:-2]+'.'+j[-2:]for j in [re.sub(r'[^\d]','',i) for i in l]]

print(remove_char(['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']))
print(remove_char(['%%$...9p2. 42', '"e"$15o.4/d9', '$29.29', ',$,5$$$9,.,25', 'E$5.0O0']))