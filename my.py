def one_punch(s):return 'Broken!' if isinstance(s,int) or len(s)==0 or type(s)==list else ' '.join(list(map(lambda e: e.replace('a','').replace('e','').replace('A','').replace('E',''),sorted(s.split()))))

print(one_punch('Friend Beer Beard Monkey Laptop'))