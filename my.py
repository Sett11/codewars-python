def is_valid(s):
    a=['_','$']
    return (s[0].isalpha() or s[0] in a) and all(map(lambda e: e in a or e.isdigit() or e.isalpha(),s[1:])) if s else 1==2

print(is_valid("okay_ok1"))
print(is_valid(""))