def cannons_ready(o):
    for i in o:
        if(o[i]=='nay'):return 'Shiver me timbers!'
    return 'Fire!'

print(cannons_ready({'Mike':'nay','Joe':'aye','Johnson':'aye','Peter':'aye'}))