def calculate(a,o,b):
    try:
        if o in '+-*/':
            return eval(f'{a}{o}{b}')
    except:
        ...