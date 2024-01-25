def reverse_complement(s):
    return s[::-1].translate(str.maketrans('TGAC','ACTG')) if all(i in 'ATGC' for i in s) else 'Invalid sequence'

print(reverse_complement('TTCCGGAA'))