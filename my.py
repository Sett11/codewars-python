def ccw(ax, ay, bx, by, cx, cy): return (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)

def graham_scan(points):
    X, Y = [], []
    points = sorted(points)
    for p in points:
        while len(X) > 1 and ccw(*X[-2], *X[-1], *p) <= 0: X.pop()
        while len(Y) > 1 and ccw(*Y[-2], *Y[-1], *p) >= 0: Y.pop()
        X.append(p), Y.append(p)
    return X,Y

def hull_method(points):
    X, Y = graham_scan(points)
    return sorted(map(list,set(map(tuple,X+Y))))

print(hull_method([[6, 20], [9, 13], [8, 6], [5, 6], [20, 4], [19, 4], [15, 19], [9, 16], [4, 11], [1, 20]]))