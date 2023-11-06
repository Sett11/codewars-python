def decode(s):
    return s.translate(str.maketrans('1234567890','9876043215'))

print(decode('4103432323'))