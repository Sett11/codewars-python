from re import match

def validate_time(s):
    return bool(match(r'^(([01][0-9])*|(2[0-3])){1,2}:([0-5][0-9])$',s)) or s=='1:00'

print(validate_time('1:59'))