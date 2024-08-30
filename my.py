from requests import get

def get_honor(s):
    return get(f'https://www.codewars.com/api/v1/users/{s}').json()['honor']

print(get_honor('jhoffner'))