def find_the_number_plate(id):
    a, n = [], id // 999
    for _ in range(3):
        a.append(chr(ord('a') + n % 26))
        n //= 26
    return ''.join(a) + str(id % 999 + 1).zfill(3)

print(find_the_number_plate(234567))
print(find_the_number_plate(43056))