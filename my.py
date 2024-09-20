from math import ceil

def waterbombs(s,w):
    return sum(ceil(len(i)/w) for i in s.split('Y'))

print(waterbombs('xxxxYxYx',4))