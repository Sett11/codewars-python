decrypt_credits = lambda s: __import__('struct').unpack('<f', bytes.fromhex(s.zfill(8)))[0]

print(decrypt_credits('803BC4'))