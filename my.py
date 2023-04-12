import re
def f(e):
    return int(e,2)
def chuck_push_ups(s):
    if(s==''):return 'CHUCK SMASH!!'
    if(isinstance(s,str)==False):return 'FAIL!!'
    if(s.find('List of jobs:')!=-1):return 'CHUCK SMASH!!'
    s=re.sub(r'[^10 ]','',s)
    if(len(s)==0):return 'CHUCK SMASH!!'
    return max(list(map(f,s.split())))

print(chuck_push_ups(1))