def spin_around(lst):
    return int(abs(sum([.25 if i == 'right' else -.25 for i in lst])))

print(spin_around(["right", "right", "right", "right", "left", "right"]))
print(spin_around(["left", "left", "left", "left"]))