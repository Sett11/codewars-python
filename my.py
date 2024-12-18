from string import ascii_uppercase as a

def get_row(n):
    n=n if n<=26 else n%26 or 26
    s=iter(a[n:])
    return ''.join(next(s) if i=='&' else i for i in (a[n-1]*n).ljust(26,'&'))

print(get_row(730548))