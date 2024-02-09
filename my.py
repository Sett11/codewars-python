from math import ceil

def aspect_ratio(x,y):
    return ceil(y/9*16),y

print(aspect_ratio(640,480))