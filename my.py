def get_number_of_squares(n):
    r=0
    i=1
    while r+i**2<n:
        r+=i**2
        i+=1
    return i-1

print(get_number_of_squares(15))