from base64 import b64encode,b64decode

def to_base_64(s):
    return b64encode(bytes(s,'utf-8')).decode().replace('=','')
    
def from_base_64(s):
    while len(s)%4:
        s+='='
    return b64decode(bytes(s,'utf-8')).decode()

print(to_base_64('this is a string!!'))
print(from_base_64('N3hReWpaaHpRcUdJcmogRXNnQ3BqLw'))