from re import match

def three_wishes(a, b, c, d):
    r = [i.replace('I want ', '') for i in [b, c, d]]
    if [i for i in r if match(r'\d+ wishes', i)]:
        return []
    for i in r:
        t, v = i.split(), False
        x = int(t[0])
        y = ' '.join(t[1:])
        if x > 1:
            y = y[:-1]
        for i in range(len(a)):
            if a[i] == y:
                while x:
                    a.insert(i, y)
                    x -= 1
                v = True
                break
        if not v:
            a.extend([y] * x)
    return a

print(three_wishes([
            'gold coin','gold coin','gold coin', 'silver coin','silver coin',
            'water','water','water','water', 'food','food','food','food',
            'book','book', 'weapon','weapon', 'clothe','clothe', 'medicine','medicine',
            'tool','tool'],
        'I want 1 food',
        'I want 2 books',
        'I want 1 girl'))