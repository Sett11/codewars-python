def odd_or_even(n):
    if(n%2!=0):return 'Either'
    return 'Odd' if (n/2)%2!=0 else 'Even'

print(odd_or_even(8))