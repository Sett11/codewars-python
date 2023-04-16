def conference_picker(a,b):
    if(len(a)==0):return b[0]
    r=list(filter(lambda e:e not in a,b))
    return r[0] if len(r) else 'No worthwhile conferences this year!'

print(conference_picker(['Mexico City','Johannesburg','Stockholm','Osaka','Saint Petersburg','London'],['Stockholm','Paris','Melbourne']))