def f(a,b):
    return  sum(i == j or i =='#' for i,j in zip(a,b)) == len(a)

def scratch(a):
    r = 0
    ans = ["tiger","rabbit","dragon","snake","rat","ox","pig","dog","cock","sheep","horse","monkey"]
    vals = ['5', '10', '20', '50', '100', '200', '500', '1000', '2000', '5000', '10000']
    for i in [i.split() for i in a]:
        if len(set(map(len,i[:-1]))) == 1:
            an, va = [j for j in ans if len(j) == len(i[0])], [j for j in vals if len(j) == len(i[-1])]
            x, y = [[f(j, k) for j in i[:-1]] for k in an], [f(i[-1], j) for j in va]
            if [j for j in range(len(x)) if all(x[j])]:
                r += int(max([va[j] for j in range(len(y)) if y[j]]))
    return r

print(scratch(['#####t #####t #####t 5##', '###### ###### ###### 1#', 'c### c### c### 5', '###### ###### ###### 5', '### #a# #a# #0#', 'c### c### ###k 1####']))