def find_ball(scales):
    for i in range(1,8,2):
        leftPan = [i-1]
        rightPan = [i]
        w = scales.get_weight(leftPan, rightPan)
        if w < 0:
            return leftPan[0]
        if w > 0:
            return rightPan[0]