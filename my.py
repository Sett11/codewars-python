def ascii_encrypt(s):
    return ''.join([chr(ord(i)+j) for j,i in enumerate(s)])
    
def ascii_decrypt(s):
    return ''.join([chr(ord(i)-j) for j,i in enumerate(s)])

print(ascii_encrypt('password'))
print(ascii_decrypt('pbuv{txk'))