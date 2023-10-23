def solve(a,b):
    return [a.count(i) for i in b]

print(solve(['abc', 'abc', 'xyz', 'cde', 'uvw'],['abc', 'cde', 'uap']))