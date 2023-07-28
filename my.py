def ranking(a):
    a,i,j=sorted(a,key=lambda e:(e['points'],-ord(e['name'][0].lower()),-ord(e['name'][1].lower()),-ord(e['name'][2].lower())),reverse=True),0,1
    while i<len(a)-1:
        a[i]['position']=j
        if a[i]['points']!=a[i+1]['points']:
            j=a.index(a[i+1])+1
        i+=1
    a[-1]['position']=j
    return a


print(ranking([
      {
        "name": "John",
        "points": 100,
      },
      {
        "name": "Bob",
        "points": 130,
      },
      {
        "name": "Mary",
        "points": 120,
      },
      {
        "name": "Kate",
        "points": 120,
      },
]))