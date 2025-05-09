import math

def ice_brick_volume(radius, bottle_length, rim_length):
    side = radius * math.sqrt(2)
    height = bottle_length - rim_length
    volume = side ** 2 * height
    return int(volume)