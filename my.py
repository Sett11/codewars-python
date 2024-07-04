from string import ascii_lowercase as a

def caeser(s,k):
    return ''.join(a[(a.index(i)+k)%26] if i in a else i for i in s).upper()

print(caeser('hello',3))