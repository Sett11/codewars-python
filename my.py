def knight_or_knave(s):
    if(isinstance(s,str)):s=eval(s)
    return 'Knight!' if s else 'Knave! Do not trust.'

print(knight_or_knave('2+2==4'))