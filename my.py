def gimme_the_letters(s):
    return ''.join([chr(i) for i in range(ord(s[0]),ord(s[-1])+1)])

print(gimme_the_letters('A-Z'))