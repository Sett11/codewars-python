from datetime import datetime,date
from calendar import monthrange

def most_frequent_days(y):
    a=[[0, 'Monday'], [0, 'Tuesday'], [0, 'Wednesday'], [0, 'Thursday'], [0, 'Friday'], [0, 'Saturday'], [0, 'Sunday']]
    for i in range(1,13):
        t=monthrange(y,i)[1]
        for j in range(1,t+1):
            a[datetime.weekday(date(y,i,j))][0]+=1
    m=max(i[0] for i in a)
    return [i[1] for i in a if i[0]==m]

print(most_frequent_days(1785))