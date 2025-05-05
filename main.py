def solve(arr):
    if not arr:
        return []
    
    roads = []
    directions = []
    
    for step in arr:
        parts = step.split(' on ')
        directions.append(parts[0])
        roads.append(parts[1])
    
    reversed_roads = roads[::-1]
    reversed_directions = ['Begin']
    
    for original_dir in directions[:0:-1]:
        if original_dir == 'Left':
            reversed_directions.append('Right')
        elif original_dir == 'Right':
            reversed_directions.append('Left')
        else:
            reversed_directions.append(original_dir)
    
    result = []
    for dir, road in zip(reversed_directions, reversed_roads):
        result.append(f"{dir} on {road}")
    
    return result