def switch_dict(d):
    o={}
    for i in d:
        o[d[i]]=[]
    for i in d:
        o[d[i]].append(i)
    return o

print(switch_dict({
          'Ice': 'Cream',
          'Age': '21',
          'Light': 'Cream',
          'Double': 'Cream'
          }))