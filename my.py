from functools import reduce
import sys
sys.set_int_max_str_digits(10000000)

def hyperfact(n):
    return reduce(lambda a,c:a*c,[i**i for i in range(1,n+1)])%1000000007
        

print(hyperfact(300))