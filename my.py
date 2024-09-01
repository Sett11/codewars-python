from functools import cache
from sys import setrecursionlimit
setrecursionlimit(2000)

@cache
def hofstadter_q(n):
   return 1 if n in [1,2] else hofstadter_q(n-hofstadter_q(n-1))+hofstadter_q(n-hofstadter_q(n-2))

print(hofstadter_q(35))