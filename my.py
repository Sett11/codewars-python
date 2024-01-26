def next_numb(n):
    if n>=9999999999:
        return "There is no possible number that fulfills those requirements"
    n+=1
    while n%3!=0:
        n+=1
    while len(str(n))!=len(set(str(n))) or n%3!=0 or n%2==0:
        n+=3
    return n

print(next_numb(712628765))