import sys
sys.set_int_max_str_digits(100000)
def get_last_digit(n):
    a,b,c=0,1,0
    while n>0:
        n-=1;c=b;b+=a;a=c
    a=str(a)
    return int(a[-1:])