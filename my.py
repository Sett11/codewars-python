def rgb_to_grayscale(c):
    h=hex(round(sum([0.299*j if i==0 else 0.587*j if i==1 else 0.114*j for i,j in enumerate([int(c[i:i+2],16) for i in range(1,len(c)+-1,2)])])))[2:]
    return '#'+(('0' if len(h)<2 else '')+h)*3


print(rgb_to_grayscale('#000000'))