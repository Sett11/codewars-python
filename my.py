def scoreboard(a):
    return sorted([{'name':i['name'],'score':i.get('chickenwings',0)*5+i.get('hamburgers',0)*3+i.get('hotdogs',0)*2} for i in a],key=lambda e:(e['score'],-ord(e['name'][0])),reverse=True)

print(scoreboard([{"name": "Joey Jaws", "chickenwings": 0, "hamburgers": 1, "hotdogs": 1},{"name": "Big Bob" , "chickenwings": 1, "hamburgers": 0, "hotdogs": 0}]))