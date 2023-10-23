from re import sub

def convert(s):
    return sub(r'[oa]',lambda e:'o' if e.group()=='a' else 'u',s)

print(convert('codewars'))