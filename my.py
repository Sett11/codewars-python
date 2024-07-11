from re import match

def which_postcode(s):
    return 'GB' if match(r'^([A-z]){1,2}(\d){1,2} (\d){1,1}([A-z]){2,2}$',s.strip()) else 'SK' if match(r'^(\d){3,3} (\d){2,2}$',s.strip()) else 'Not valid'

print(which_postcode('Se21 7aA'))
print(which_postcode('123 45'))
print(which_postcode('123 45j'))