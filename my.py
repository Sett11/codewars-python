def sexy_name(s):
    n=sum(SCORES.get(i.upper(),0) for i in s)
    return 'NOT TOO SEXY' if n<=60 else 'PRETTY SEXY' if n<=300 else 'VERY SEXY' if n<600 else 'THE ULTIMATE SEXIEST'
