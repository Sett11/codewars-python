from math import floor,log10,pi,e

# Kamenetsky formula
factor_digit=lambda n:1 if n<2 else floor(n*log10(n/e)+log10(2*pi*n)/2)+1

print(factor_digit(777))