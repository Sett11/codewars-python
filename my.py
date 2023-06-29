def last_fib_digit(n,q=5**0.5):
    return round(((1+q)/2)**(n%60)/q)%10

print(last_fib_digit(302))