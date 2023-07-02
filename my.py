def fillable(s,m,n):
    try:
        return s[m]>=n
    except:
        return False

print(fillable({
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 },'football',3))
print(fillable({
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 },'leggos',2))