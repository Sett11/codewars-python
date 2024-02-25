even_odd=lambda lst:__import__('functools').reduce(lambda a,c:a*c[1] if c[0]&1 else a+c[1],enumerate(lst),0)

print(even_odd([1,2,6,1,6,1,3,9,6]))