def sticky_calc(o,a,b):
    a,b=str(round(a)),str(round(b))
    return round(eval(f'{a+b}{o}{b}'))


print(sticky_calc('+',75,5))