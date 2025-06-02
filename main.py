def number_lappings(my_speed, ghost_speed, time, round_length):
    if my_speed <= ghost_speed:
        return 0
    relative_distance = (my_speed - ghost_speed) * time
    full_laps = relative_distance // round_length
    if relative_distance == full_laps * round_length:
        return max(0, full_laps - 1)
    else:
        return int(full_laps)