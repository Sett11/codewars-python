from re import sub
from collections import OrderedDict

def lottery(s):
    return ''.join(OrderedDict.fromkeys(sub(r'\D','',s))) or 'One more run!'


print(lottery('hPrBKWDH8yc6Lt5NQZWQ'))