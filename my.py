def format_playlist(s):
    a,m1,m2=sorted(s,key=lambda e:(e[2],e[0])),max([len(i[0]) for i in s],default=4),max([len(i[2]) for i in s],default=6)
    e,e2='+'+'-'*(m1+2)+'+'+'-'*6+'+'+'-'*(m2+2)+'+','| '+'Name'+' '*(m1-4)+' |'+' Time | '+'Artist'+' '*(m2-6)+' |'
    r=[e,e2,e]
    for i in a:
        r.append('| '+i[0]+' '*(m1-len(i[0]))+' | '+i[1]+' | '+i[2]+' '*(m2-len(i[2]))+' |')
    return '\n'.join(r)+(('\n'+e) if len(s) else '')

print(format_playlist([
                    ('Stoned Again', '3:25', 'King Krule'),
                    ('Serenade', '3:00', 'Travis Scott'),
                    ('I Always Wanna Die (Sometimes)', '5:15', 'The 1975'),
                    ('Stick Talk', '2:54', 'Future'),
                    ('Nightcrawler', '5:22', 'Travis Scott')]))