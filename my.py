import numpy as np
from re import sub

def encrypt(text, key):
    f = lambda x:ord(x) - 97
    ar = np.array(list(map(f, list(key)))).reshape(2, 2)
    s = sub(r'[^a-z]', '', text.lower())
    s += 'z' if len(s)&1 else ''
    mat = np.array([list(map(f, [s[i], s[i+1]])) for i in range(0, len(s), 2)])
    result = [ar @ i for i in mat]
    return ''.join(chr(x%26 + 97) for row in result for x in row).upper()

print(encrypt('This is a good day','bbaa'))
print(encrypt('Hi','cats'))