def calc_fuel(n):
    n*=11
    o={"lava": 800, "blaze rod": 120, "coal": 80, "wood": 15, "stick": 1}
    r={"lava": 0, "blaze rod": 0, "coal": 0, "wood": 0, "stick": 0}
    for i in o:
        while n>=o[i]:
            r[i]+=1
            n-=o[i]
    return r

print(calc_fuel(37))