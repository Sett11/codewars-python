import math
def pop_shift(s):
    return [s[math.floor(len(s)/2)+1:][::-1],s[:math.ceil(len(s)/2)-1],s[math.floor(len(s)/2)]] if len(s)%2!=0 else [s[int(len(s)/2):][::-1],s[:int(len(s)/2)],'']

print(pop_shift('letstalkaboutjavascriptthebestlanguage'))