change_me=lambda s:{'£5':' '.join(['20p']*25),'£2':' '.join(['20p']*10),'£1':' '.join(['20p']*5),'50p':'20p 20p 10p','20p':'10p 10p'}.get(s,s)

print(change_me('£5'))