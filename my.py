def f(a):
    r=[]
    m=-1
    l=len(a)
    for i in range(l):
        t,c=a[i]['name'],a[i]['age']
        for j in range(i+1,l):
            if a[j]['name']==t:
                c+=a[j]['age']
        r.append([t,c])
        m=max(m,c)
    return sorted([i[0] for i in r if i[1]==m])[0]

def highest_age(o1,o2):
    return f(o1+o2)

print(highest_age([{'name': 'Katsutoshi Imai', 'age': 9}, {'name': 'Taro Koyama', 'age': 8}, {'name': 'Suenaga', 'age': 3}, {'name': 'Shinji Ito', 'age': 6}, {'name': 'Ryo Tanaka', 'age': 15}, {'name': 'Satoshi Katakiri', 'age': 16}, {'name': 'Shinji Ito', 'age': 11}, {'name': 'Yuichi Sakakigawa', 'age': 16}, {'name': 'Taro Koyama', 'age': 15}] , [{'name': 'Shinji Ito', 'age': 1}, {'name': 'Ryo Tanaka', 'age': 10}, {'name': 'Ryo Tanaka', 'age': 4}, {'name': 'Satoshi Katakiri', 'age': 5}, {'name': 'Yasuo Tanigawa', 'age': 10}, {'name': 'Ryo Tanaka', 'age': 5}]))