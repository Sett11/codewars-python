from datetime import datetime

def convert(t):
    s=str(t).split(' ')[-1].split('.')
    return s[0]+',000' if len(s)==1 else ','.join(s)[:-3]

print(convert(datetime(2016, 2, 8, 16, 42, 59,399000)))
print(convert(datetime(2016, 2, 8, 16, 42, 59,10)))
print(convert(datetime(2016, 2, 8, 16, 42, 59)))