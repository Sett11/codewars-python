def case_id(s):
    print(s)
    if '--' in s or '__' in s or ('-' in s and '_' in s) or(('-' in s or '_' in s) and [i for i in s if i.isupper()]):
        return 'none'
    a,b=s.split('-'),s.split('_')
    if len(a)>1 and not [i for i in a if i[0].isupper()]:
        return 'kebab'
    if len(b)>1 and not [i for i in b if i[0].isupper()]:
        return 'snake'
    return 'camel' if [i for i in s if i.isupper()] and not [i for i in s if i in ['_','-']] else 'none'

print(case_id("hello-to-the-world"))
print(case_id("helloWorld"))
print(case_id("hello_world"))
print(case_id("hello-World"))