def f(x):
    l = 'aioueyAIOUEY'
    r = 'kontti'
    i = 0
    while l.find(x[i]) == -1:
        i += 1
        if (i >= len(x)):
            break
    return 'ko'+x[i+1:]+'-'+x[:i+1]+r'ntti' if i < len(x) else x


def kontti(s):
    return ' '.join(map(f, s.split()))


print(kontti("aeiou"))
