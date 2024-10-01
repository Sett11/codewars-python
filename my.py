def traffic_count(a):
    a,b,c,d=[a[i:i+6] for i in range(0,len(a),6)]
    return [('4:00pm',max(a)),('5:00pm',max(b)),('6:00pm',max(c)),('7:00pm',max(d))]

print(traffic_count([23,24,34,45,43,23,57,34,65,12,19,45, 54,65,54,43,89,48,42,55,22,69,23,93]))