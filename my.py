def flatten(d):
    r={}
    def f(x,s):
        if isinstance(x,str) or not x:
            r[s]=x if x else ''
            return
        for i in x:
            f(x[i],s+'/'+i)
    for i in d:
        f(d[i],i)
    return r 
        

print(flatten({
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"
        }
    }
}))