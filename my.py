def passer_rating(att, yds, comp, td, ints):
    a=((comp/att)-0.3)*5
    b=((yds/att)-3)*0.25
    c=(td/att)*20
    d=2.375-((ints/att)*25)
    if(a>2.375):a=2.375
    if(b>2.375):b=2.375
    if(c>2.375):c=2.375
    if(d>2.375):d=2.375
    if(a<0):a=0
    if(b<0):b=0
    if(c<0):c=0
    if(d<0):d=0
    return round(((a+b+c+d)/6)*100,1)

print(passer_rating(432, 3554, 291, 28, 2))