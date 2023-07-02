def format_money(n):
    n=str(float(n))
    if len(n[n.index('.')+1:])<2:
        n+='0'
    return '$'+n

print(format_money(198))
print(format_money(3))