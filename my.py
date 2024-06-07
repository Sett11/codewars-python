from math import pi

def sum_circles(*args):
    return f"We have this much circle: {round(sum(pi*i**2/4 for i in args))}"

print(sum_circles(2,3,4))