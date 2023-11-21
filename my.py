def cheapest_quote(n):
    o={40:3.85,20:1.93,10:.97,5:.49,1:.10}
    s=0.00

    for i in o:
        t,p=divmod(n,i)
        s+=o[i]*t
        n=p

    return round(s,2)


print(cheapest_quote(44))
print(cheapest_quote(80))
print(cheapest_quote(26))
print(cheapest_quote(54))