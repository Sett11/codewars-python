def solve(before, after):
    avg_before, dist_before = before
    avg_after, dist_after = after
    
    total_fuel_before = (avg_before * dist_before) / 100
    total_fuel_after = (avg_after * dist_after) / 100
    
    fuel_during = total_fuel_after - total_fuel_before
    dist_during = dist_after - dist_before
    
    avg_during = (fuel_during / dist_during) * 100 if dist_during != 0 else 0.0
    
    return round(avg_during, 1)