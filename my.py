from functools import reduce

def did_we_win(a):
    return reduce(lambda c,e:c+(e[0] if e and ('pass' in e or 'run' in e) else -e[0] if e else 0),a,0)>10


print(did_we_win([[8, "pass"],[5, "sack"],[3, "sack"],[5, "run"]]))
print(did_we_win([[2, "run"],[5, "pass"],[3, "sack"],[8, "pass"]]))
print(did_we_win([[12, "pass"],[],[],[]]))