def fizz_buzz_cuckoo_clock(t):
    a=[int(i) for i in t.split(':')]
    a[0]=a[0] if a[0] else 12
    return ('Cuckoo '*(a[0]%(12 if a[0]!=12 else 13))).rstrip() if not a[1] else 'Cuckoo' if a[1]==30 else 'Fizz Buzz' if not a[1]%5 and not a[1]%3 else 'Fizz' if not a[1]%3 else 'Buzz' if not a[1]%5 else 'tick'

print(fizz_buzz_cuckoo_clock("11:15" ))
print(fizz_buzz_cuckoo_clock("00:00" ))
print(fizz_buzz_cuckoo_clock("12:00" ))
print(fizz_buzz_cuckoo_clock("08:55" ))