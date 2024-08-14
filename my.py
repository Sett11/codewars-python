from scipy.spatial import ConvexHull

def convex_hull_area(p):
    try:
        return round(ConvexHull([[str(j) for j in i] for i in p]).volume,2)
    except:
        return 0

print(convex_hull_area({(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0)}))