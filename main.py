def calculate_damage(y, o, n, m):
    r, t = 50 * (n / m), {'>':2, '==': 1, '<': .5}
    if y == o:
        return r * .5
    a = ['fire > grass', 'fire < water', 'fire == electric', 'water < grass', 'water < electric', 'grass == electric', 'grass < fire', 'water > fire', 'grass > water', 'electric > water', 'electric == fire', 'electric == grass']
    return r * t[[i.split()[1] for i in a if (s := i.split())[0] == y and s[-1] == o][0]]
    
print(calculate_damage("fire", "water", 100, 100))