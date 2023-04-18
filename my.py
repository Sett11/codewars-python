def get_the_vowels(s):
    v = list('aeiou')
    i = 0
    j = 0
    c = 0
    while i < len(s):
        if (s[i] == v[j % len(v)]):
            c += 1
            j += 1
        i += 1
    return c


print(get_the_vowels('akfheujfkgiaaaofmmfkdfuaiiie'))
