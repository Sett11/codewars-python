def f(e):return int(e)
def get_sum_of_digits(num):
    d=map(f,list(str(num)))
    return sum(list(d))

print(get_sum_of_digits(123))