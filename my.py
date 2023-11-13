def num_of_open_lockers(n):
    return len([i for i in range(int(n**.5))])


print(num_of_open_lockers(128))
print(num_of_open_lockers(56))