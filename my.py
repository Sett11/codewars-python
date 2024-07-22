from re import sub

def is_turing_equation(s):
	return eval(sub(r'\d+',lambda x:str(int(x.group()[::-1])),s.replace('=','==')))

print(is_turing_equation('73+42=16'))