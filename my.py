def most_common(s):
    return ''.join(sorted(s,key=lambda x:s.count(x),reverse=True))

print(most_common('Hello world'))