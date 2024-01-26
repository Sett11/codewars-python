songs=[{'artist': 'Marillion', 'title': 'Keyleigh', 'playback': '03:36'}, {'artist': 'Pink Floyd', 'title': 'Time', 'playback': '06:48'}, {'artist': 'Rush', 'title': 'YYZ', 'playback': '04:27'}, {'artist': 'Bonobo', 'title': 'Days To Come', 'playback': '03:50'}, {'artist': 'Coldplay', 'title': 'Yellow', 'playback': '04:32'}, {'artist': 'Bloc Party', 'title': 'Like Eating Glass', 'playback': '04:22'}, {'artist': 'The Killers', 'title': 'For Reasons Unknown', 'playback': '03:30'}, {'artist': 'Arctic Monkeys', 'title': 'Teddy Picker', 'playback': '03:25'}, {'artist': 'Joe Satriani', 'title': 'Surfing With The Alien', 'playback': '04:34'}]

def longest_possible(n):
    r=[]
    for i in songs:
        a,b=i['playback'].split(':')
        k=int(a)*60+int(b)
        if k<=n:
            r.append(i)
    r=sorted(r,key=lambda x:x['playback'],reverse=True)
    return bool(r) and r[0]['title']

print(longest_possible(215))
print(longest_possible(270))
print(longest_possible(15))