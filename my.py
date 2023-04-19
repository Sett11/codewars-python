def find_the_strongest_apes(l):
    one=sorted(list(map(lambda e:[e['weight']+e['height'],e['name']],list(filter(lambda e:e['type']=='Gorilla',l)))))
    two=sorted(list(map(lambda e:[e['weight']+e['height'],e['name']],list(filter(lambda e:e['type']=='Gibbon',l)))))
    three=sorted(list(map(lambda e:[e['weight']+e['height'],e['name']],list(filter(lambda e:e['type']=='Orangutan',l)))))
    four=sorted(list(map(lambda e:[e['weight']+e['height'],e['name']],list(filter(lambda e:e['type']=='Chimpanzee',l)))))
    one.sort(key=lambda e:e[0],reverse=True)
    two.sort(key=lambda e:e[0],reverse=True)
    three.sort(key=lambda e:e[0],reverse=True)
    four.sort(key=lambda e:e[0],reverse=True)
    return {'Gorilla': (one[0][1] if len(one) else None), 'Gibbon': (two[0][1] if len(two) else None), 'Orangutan': (three[0][1] if len(three) else None), 'Chimpanzee': (four[0][1] if len(four) else None)}

print(find_the_strongest_apes(  [{"name": "aba", "weight": 10, "height": 50, "type": "Gibbon"},
             {"name": "abb", "weight": 15, "height": 60, "type": "Gibbon"},
             {"name": "abc", "weight": 20, "height": 50, "type": "Gibbon"},
             {"name": "abd", "weight": 50, "height": 100, "type": "Chimpanzee"}]))