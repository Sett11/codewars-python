def to_integer(s):
    try: return int(s,(2 if '0b' in s else 8 if '0o' in s else 16 if '0x' in s else 10)) if all(i not in s for i in [' ','\n']) else None
    except:pass

print(to_integer('123'))