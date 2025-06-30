from statistics import mean

def get_min_avg_max(k, a):
    r, q = [], []
    for i in a:
        t = i[k:-k]
        r.append((min(t), mean(t), max(t)))
        q.extend(t)
    return r + [(min(q), mean(q), max(q))]

print(get_min_avg_max(2, [[800, 1200, 2100, 4100, 1300, 700], [1000, 1500, 4500, 5000, 5800, 2000, 1500]]))