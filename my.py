def get_los_angeles_points(a):
    s=0
    for i,j in a:
        t=i.split()
        if i.startswith('Los Angeles ') and t[-1].isalpha() and t[-1].istitle() and t[-1][1:].islower() and len(t)==3:
            s+=int(j.split(':')[0])
    return s

print(get_los_angeles_points([
          ["Golden State Warriors", "559:503"],
          ["Memphis Grizzlies", "550:511"],
          ["Portland Trail Blazers", "527:520"],
          ["Houston Rockets", "494:458"],
          ["San Antonio Spurs", "469:460"],
          ["Phoenix Suns", "523:522"],
          ["Minnesota Timberwolves", "495:494"],
          ["Utah Jazz", "399:402"],
          ["Sacramento Kings", "420:431"],
          ["Denver Nuggets", "646:658"],
          ["Los Angeles Clippers", "382:422"],
          ["Dallas Mavericks", "492:513"],
          ["Los Angeles Lakers", "641:637"],
          ["Oklahoma City Thunder", "315:318"],
          ["New Orleans Pelicans", "433:454"]
        ]))