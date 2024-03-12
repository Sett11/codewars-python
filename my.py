from requests import get
from re import findall

def get_leaderboard_honor():
    return list(map(lambda x:int(x[1:-1].replace(',','')),findall(r'>\d+,\d+<',get('https://www.codewars.com/users/leaderboard').content.decode())))