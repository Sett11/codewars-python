from re import sub

def der_die_das(s):
    n=len(sub(r'[^aieouäöü]','',s.lower()))
    if n<2:
        return 'das '+s
    if n>3:
        return 'der '+s
    return 'die '+s
    