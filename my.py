def fix_code(s):
    try:
        return next(str(i) for i in range(10) if sum(int(j)*(10-k) if j!='X' else 10 for k,j in enumerate(s.replace('?',str(i))))%11==0)
    except StopIteration:
        return 'X'

print(fix_code('020161586?'))