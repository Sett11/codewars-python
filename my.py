from re import sub

def get_users_ids(s):
    return [sub(r'^uid','',i.lower().replace('#','').strip()).strip() for i in s.strip().split(', ')]

print(get_users_ids("uid12 abuid, uid#, uidMiXeDcHaRs"))