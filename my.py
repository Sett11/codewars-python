from re import sub

def bin_str(s):
    if '1' not in s:
        return 0
    c=0
    while '1' in s:
        i=s.index('1')
        s=sub(r'.',lambda e:'1' if e.group()=='0' else '0',s[i:])
        c+=1
    return c

print(bin_str("11111000011111"))
print(bin_str("000001111100000"))