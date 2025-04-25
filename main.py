def travel_distance(avg_speed, travel_time):
    KM_PER_KNOT = 1.852
    travel_hours = travel_time / 60
    travel_kms = avg_speed * KM_PER_KNOT * travel_hours
    return travel_kms