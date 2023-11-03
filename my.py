from re import sub

def timed_reading(l,t):
    return len(list(filter(lambda e:len(e)<=l and e,map(lambda e:sub(r'[^A-z]','',e),t.split(' ')))))