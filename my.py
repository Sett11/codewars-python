def is_onion_array(a):
    return all([a[i]+a[len(a)-1-i]<=10 for i in range(len(a)//2)])

print(is_onion_array([-13, -37, -95, -53, -68, 65, 61, 89, 43, 5]))
print(is_onion_array([58, 14, 6, 59, 3, 42, -8, -54, -7, -11, -55]))
print(is_onion_array([1, 1, 15, 10, -1]))