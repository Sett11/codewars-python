def pathfinder_scores(s):
    try:
        a={7:-4,8:-2,9:-1,10:0,11:1,12:2,13:3,14:5,15:7,16:10,17:13,18:17}
        return sum([a[i] for i in s])<=25
    except:
        return False

print(pathfinder_scores([18, 13, 7, 12, 15, 10]))