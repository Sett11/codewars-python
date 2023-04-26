def largest_power(n):
    i=0
    while True:
        if(3**i>=n):
            return i-1
        i+=1

print(largest_power(4))