def find_next_power(n,p):
    return int(pow(n,(1/p))+1)**p

print(find_next_power(1245678,5))
print(find_next_power(12385, 3))