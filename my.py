from hashlib import sha256
from itertools import permutations

def sha256_cracker(h,s):
    try:
        return next(j for j in [''.join(i) for i in permutations(s)] if sha256(bytes(j,encoding='utf-8')).hexdigest()==h)
    except:
        pass

print(sha256_cracker('5694d08a2e53ffcae0c3103e5ad6f6076abd960eb1f8a56577040bc1028f702b','cdeo'))