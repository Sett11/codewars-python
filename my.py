def bear_dollars(a):
    d={'close friend':25,'friend':50,'acquaintance':100}
    return sum(i[0]*d.get(i[1].lower(),125) for i in a)

print(bear_dollars([(10, 'Close Friend'), (3, 'Acquaintance'), (7, 'Lead from web'), (6, 'Friend'), (2, 'From advertisements')]))