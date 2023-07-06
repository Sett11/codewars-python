def tax_calculator(t):
    try:
        c=0
        if t<=0:
            1/0
        while t:
            if t<=10:
                c+=t/10
                t=0
            if t<=20 and t>=10:
                x=t-10
                c+=x/100*7
                t-=x
            if t<=30 and t>=20:
                x=t-20
                c+=x/100*5
                t-=x
            if t>30:
                x=t-30
                c+=x/100*3
                t-=x
        return int(c) if int(c)==c else round(c,2)
    except:
        return 0

print(tax_calculator(10))