from functools import reduce
def multi(l_st):
    return reduce(lambda a,c:a*c,l_st)
def add(l_st):
    return sum(l_st)
def reverse(string):
    return string[::-1]

print(reverse("Hello World"))