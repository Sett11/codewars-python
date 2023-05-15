def number_to_ordinal(n):
    n=str(n)
    if(n=='0'):
        return n
    if(n[-2:]=='11' or n[-2:]=='12' or n[-2:]=='13'):
        return n+'th'
    if(n[-1:]=='1'):
        return n+'st'
    if(n[-1:]=='2'):
        return n+'nd'
    if(n[-1:]=='3'):
        return n+'rd'
    return n+'th'

print(number_to_ordinal(20011))