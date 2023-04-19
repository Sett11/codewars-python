def infected(s):
    s=list(''.join(list(map(lambda e: '1'*len(e) if '1' in e else e,list(filter(lambda e:e,s.split('X')))))))
    return 100*len(list(filter(lambda e:e=='1',s)))/len(s) if len(s) else 0

print(infected("XXXXXXX"))