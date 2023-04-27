import hashlib as h

def to_sha256(s):
    return h.sha256(bytes(s,encoding='utf-8')).hexdigest()

print(to_sha256('Hello World!'))