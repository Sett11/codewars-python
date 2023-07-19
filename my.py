from datetime import datetime

def is_today(d):
    return datetime.today().date()==d.date()

print(is_today(datetime.today()))