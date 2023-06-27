o={1000: 'thousand', 100: 'hundred', 90: 'ninety', 80: 'eighty', 70: 'seventy', 60: 'sixty', 50: 'fifty', 40: 'forty', 30: 'thirty', 20: 'twenty', 19: 'nineteen', 18: 'eighteen', 17: 'seventeen', 16: 'sixteen', 15: 'fifteen', 14: 'fourteen', 13: 'thirteen', 12: 'twelve', 11: 'eleven', 10: 'ten', 9: 'nine', 8: 'eight', 7: 'seven', 6: 'six', 5: 'five', 4: 'four', 3: 'three', 2: 'two', 1: 'one'}

def f(n):
    a=[]
    for i in o:
        t=[]
        while n>=i:
            n-=i
            t.append(o[i])
        if len(t):
            a.append([o[len(t)] if o.get(len(t)) else f(len(t)),t[0]] if i>=100 else t[0])
    return a

def r(x):
    a=[]
    [a.append(i) if type(i)!=list else a.extend(r(i)) for i in x]
    return a

def number_to_english(n):
    if not n:
        return 'zero'
    return ' '.join(r(f(n))) if type(n)==int and n>-1 and n<100000 else ''

print(number_to_english(573982))