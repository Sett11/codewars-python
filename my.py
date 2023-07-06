def match(c,j):
    return c['min_salary']/100*90<=j['max_salary']

print(match({ 'min_salary': 120000 },{ 'max_salary': 130000 }))