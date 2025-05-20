def count_min_rotations(dice):
    opposite = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    min_rotations = float('inf')
    
    for target in range(1, 7):
        total = 0
        for face in dice:
            if face == target:
                continue
            if opposite[face] == target:
                total += 2
            else:
                total += 1
        if total < min_rotations:
            min_rotations = total
    return min_rotations