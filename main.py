from math import ceil

def who_would_win(o1, o2):
    f, w, c = lambda x : ceil(x["number"]) * x["damage"], lambda x: x["number"] * x["hitpoints"], 1
    while o1["number"] > 0 and o2["number"] > 0:
        if c & 1:
            o2["number"] = (w(o2) - f(o1)) / o2["hitpoints"]
        else:
            o1["number"] = (w(o1) - f(o2)) / o1["hitpoints"]
        c += 1
    if (r := o1["number"]) > 0:
        return f'{ceil(r)} {o1["type"]}(s) won'
    return f'{ceil(o2["number"])} {o2["type"]}(s) won'
            

print(who_would_win({ "type": "Roc", "hitpoints": 40, "number": 6, "damage":8 },
     { "type": "Unicorn", "hitpoints": 40, "number": 4, "damage":13}))
print(who_would_win({ "type": "Titan",       "hitpoints": 300,"number": 1, "damage":50},
     { "type": "Battle Dwarf","hitpoints": 20, "number": 25,"damage":4}))
print(who_would_win({ "type": "Paladin",     "hitpoints": 50, "number": 8 , "damage":20},
     { "type": "Skeleton",    "hitpoints": 4 , "number": 100,"damage":3 }))