def get_percentage(n,l=1000):
    return "No e-mails sent" if not n else "Daily limit is reached" if n>=l else str(int(n//(l/100)))+'%'

print(get_percentage(502,920))
print(get_percentage(256,500))