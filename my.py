def snapshot(s):
    if len(s)<11 or len(set(s))<3:
        return s
    if s[0] not in '.·' or s[-1] not in '.·':
        v=s[0] not in '.·'
        a=list(s if v else s[::-1])
        a[5]='x'
        a[9]=a[10]=']' if v else '['
        r='[['+''.join(a[2:])
        return r if v else r[::-1][:-2]+']]'
    if 'seagull' in s:
        g=s.find('seagull')
        return s[:g-2]+'[[seaxull]]'+s[g+9:]

print(snapshot('gull.·..······..·'))