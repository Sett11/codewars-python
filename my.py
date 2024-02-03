def could_be(o,a):
    o,a=o.split(),a.split()
    return bool(a and o) and all(i in o for i in a)

print(could_be('Carlos Ray Norris','Carlos Norris'))