from collections import Counter
from re import sub

def dead_ant_count (s):
    return max(Counter(sub(r'[^A-z]','',''.join([i for i in s.split('ant') if any(j.isalpha() for j in i)]))).values(),default=0)

print(dead_ant_count("ant anantt aantnt"))
print(dead_ant_count('...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t'))
print(dead_ant_count('antantantan'))