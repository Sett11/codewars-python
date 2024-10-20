from bisect import bisect as bs

def leaderboard_climb(arr,kara):
    n,a,b=len(kara),sorted(set(arr)),kara[:]
    for i in range(n):
        b[i]=(len(a)-bs(a,b[i])+1) or 1
    return b
        

print(leaderboard_climb([92, 83, 80, 69, 64, 55, 52, 42, 39, 36, 28, 17, 12, 1], [4, 5, 14, 23, 27, 28, 35, 44, 46, 50, 56, 58, 61, 67, 74, 81, 88, 88, 90, 96, 100, 100]))
