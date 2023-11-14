def generate_currency_matrix(c):
    a=["EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"]
    return [j for j in [c+i if a.index(c)<a.index(i) else i+c for i in a] if j!=c+c]