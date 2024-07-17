valid_mersenne=lambda x:__import__('gmpy2').is_prime(2**x-1)

print(valid_mersenne(127))