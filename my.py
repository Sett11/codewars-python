def comfortable_word(s):
    a,b='qwertasdfgzxcvb','yuiophjklnm'
    return all(s[i] in (b if i&1 else a) for i in range(len(s))) or all(s[i] in (a if i&1 else b) for i in range(len(s)))

print(comfortable_word('yams'))