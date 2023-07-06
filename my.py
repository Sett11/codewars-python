import re
def we_rate_dogs(s,r):
    return re.sub(r'\d+\/',str(r)+'/',s)

print(we_rate_dogs('This is Tucker. He would like a hug. 3/10 someone hug him',11))