def bear_fur(l):
    return {('black', 'black'):'black',
    ('brown', 'brown'):'brown',
    ('white', 'white'):'white',
    ('black', 'brown'):'dark brown',
    ('black', 'white'):'grey',
    ('brown', 'white'):'light brown'}.get(tuple(sorted(l)),'unknown')

print(bear_fur(['brown', 'white']))