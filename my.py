def ordinal(n,b=False):
    n=str(n)
    if(n=='0'):
        return 'th'
    if(n[-2:]=='11' or n[-2:]=='12' or n[-2:]=='13'):
        return 'th' if not b else 'th'
    if(n[-1:]=='1'):
        return 'st' if not b else 'st'
    if(n[-1:]=='2'):
        return 'nd' if not b else 'd'
    if(n[-1:]=='3'):
        return 'rd' if not b else 'd'
    return 'th' if not b else 'th'

print(ordinal(22))