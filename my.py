from collections import OrderedDict

def unite_unique(*a):
    return list(OrderedDict.fromkeys(sum(list(a),[])))


print(unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]))