

# from gmpy2 import next_prime

# def gen_prime(n,p=2):
#     while n:
#         yield p
#         x=int(next_prime(p))
#         p=x
#         n-=1

# def get_primes(n,m=2):
#     g=gen_prime(n)
#     for _ in range(0,n,m):
#         t=[]
#         for __ in range(m):
#             t.append(next(g,None))
#         yield tuple(t)

# g=get_primes(11,5)
# print([next(g) for _ in range(3)])