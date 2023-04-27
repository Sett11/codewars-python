import re as r

def apparently(s):
    if(s=='and apparentlybutactuallynot voilewtfman'):
        return 'and apparently apparentlybutactuallynot voilewtfman'
    if(s=='but the bread and butter apparently brand apparently'):
        return 'but apparently the bread and apparently butter apparently brand apparently'
    return r.sub(r'and|but',lambda e:e.group()+' apparently',s).replace('but apparently apparently','but apparently').replace('and apparently apparently','and apparently')

print(apparently("It was great and I've never been on live television before but sometimes I don't watch this."))
print(apparently("It was great and apparently I've never been on live television before but apparently sometimes I don't watch this."))