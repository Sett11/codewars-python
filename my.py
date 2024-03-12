from requests import get
from html.parser import HTMLParser


a=[]

class Html(HTMLParser):
    def handle_starttag(self,tag,attrs):
        for i,j in attrs:
            if i=='data-username':
                a.append(j)

def f():
    return get('https://www.codewars.com/users/leaderboard').text

h=Html()

for i in f():
    h.feed(i)


def get_codeChallenges(n):
    g=get('https://www.codewars.com/api/v1/users/'+a[n-2]).json()["codeChallenges"]
    return [g["totalAuthored"],g["totalCompleted"]]

print(get_codeChallenges(55))