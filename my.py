import math

def is_in_middle(s):
    return s[math.floor(len(s)/2)-1:math.ceil(len(s)/2)+1]=='abc' or s[math.floor(len(s)/2)-2:math.ceil(len(s)/2)+1]=='abc' or s[math.floor(len(s)/2)-1:math.ceil(len(s)/2)+2]=='abc'

print(is_in_middle('AabcBB'))
print(is_in_middle('abcabcabc'))