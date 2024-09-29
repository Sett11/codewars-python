from re import sub

def proofread(s):
    return sub(r'\.\s[a-z]',lambda x:x.group().upper(),s.lower().replace('ie','ei').capitalize())

print(proofread("Niether of the fencers wanted to forfiet the match. They both expected to sieze victory."))