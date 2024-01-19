def counter():
    count=0
    def f():
        nonlocal count
        count+=1
        return count
    return f

counter_one = counter()
counter_two = counter()

print(counter_one())
print(counter_one())
print(counter_two())
print(counter_two())