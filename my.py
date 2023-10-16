def premier_league_standings(o):
    one=o[1]
    del o[1]
    return dict(zip([i for i in range(1,len(o)+2)],([one]+sorted(o.values()))))

print(premier_league_standings({1: 'Leeds United', 2: 'Liverpool', 3: 'Manchester City', 4: 'Coventry', 5: 'Arsenal'}))