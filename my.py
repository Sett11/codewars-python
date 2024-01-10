from hashlib import sha1
from string import ascii_lowercase as a
from functools import cache

@cache
def pr(*a):
    return {()} if not a else [''.join([i]+list(j)) for i in a[0] for j in pr(*a[1:])]

b=[pr(a,a),pr(a,a,a),pr(a,a,a,a),pr('abcd',a,a,a,a)]

def password_cracker(s):
    for i in range(len(b)):
        for j in range(len(b[i])):
            if sha1(bytes(b[i][j],'utf-8')).hexdigest()==s:
                return b[i][j]
        

print(password_cracker('e6fb06210fafc02fd7479ddbed2d042cc3a5155e'))