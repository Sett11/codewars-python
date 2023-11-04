from re import sub

def get_weight(s):
    return sum(map(ord,sub(r'.',lambda e: e.group().lower() if e.group().isupper() else e.group().upper(),sub(r'\W|\d|_','',s))))


print(get_weight('Joe'))