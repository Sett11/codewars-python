o={1000: 'thousand', 100: 'hundred', 90: 'ninety', 80: 'eighty', 70: 'seventy', 60: 'sixty', 50: 'fifty', 40: 'forty', 30: 'thirty', 20: 'twenty', 19: 'nineteen', 18: 'eighteen', 17: 'seventeen', 16: 'sixteen', 15: 'fifteen', 14: 'fourteen', 13: 'thirteen', 12: 'twelve', 11: 'eleven', 10: 'ten', 9: 'nine', 8: 'eight', 7: 'seven', 6: 'six', 5: 'five', 4: 'four', 3: 'three', 2: 'two', 1: 'one'}


def number2words(n):
    a=[]
    for i in o:
        t,p=divmod(n,i)
        if t!=0:
            a.append(f'{o.get(t,number2words(t))} {o[i]}' if t>1 or i in [1000,100] else o[i])
            n=p
    return ' '.join(a).replace('ty ','ty-').replace('ty-thousand','ty thousand') or 'zero'

print(number2words(58543))
print(number2words(565058))