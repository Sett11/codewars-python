from itertools import combinations_with_replacement as comb,permutations as perm

ops=sum([list(set(perm(i))) for i in comb('+-/*',3)],[])
templates=['{0} {4} {1} {5} {2} {6} {3}',
    '({0} {4} {1}) {5} ({2} {6} {3})',
    '{0} {4} ({1} {5} {2}) {6} {3}',
    '({0} {4} {1}) {5} {2} {6} {3}',
    '({0} {4} {1} {5} {2}) {6} {3}',
    '(({0} {4} {1}) {5} {2}) {6} {3}',
    '({0} {4} ({1} {5} {2})) {6} {3}',
    '{0} {4} {1} {5} ({2} {6} {3})',
    '{0} {4} ({1} {5} {2} {6} {3})',
    '{0} {4} (({1} {5} {2}) {6} {3})',
    '{0} {4} ({1} {5} ({2} {6} {3}))']

def f(a):
    for i in a:
        for op in ops:
            for temp in templates:
                s=temp.format(*list(map(str,i)),*op)
                try:
                    if eval(s)==24:
                        return s
                except:
                    pass

def equal_to_24(*a):
    return f(list(perm(a))) or "It's not possible!"