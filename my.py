def distinct_digit_year(n):
    while True:
        n+=1
        if len(set(str(n)))==len(str(n)):
            return n