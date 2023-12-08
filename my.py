from datetime import datetime
from hashlib import md5

def geohash(dow,date=datetime.now()):
    s=str(dow)
    if len(s.split('.')[1])<2:
        s+='0'
    h=md5(bytes(date.strftime('%Y-%m-%d-')+s,encoding='utf-8')).hexdigest()
    return [round(float.fromhex('0.'+h[0:16]),6),round(float.fromhex('0.'+h[16:]),6)]


print(geohash(10458.68, datetime(2005,5,26)))