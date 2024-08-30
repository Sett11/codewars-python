from requests import get
from re import compile

def get_member_since(s):
   r=get(f'https://www.codewars.com/users/{s}')
   for i in r.iter_lines():
      t=compile(r'\w{3}\s\d{4}').search(i.decode().strip())
      if t:
         return t.group()

print(get_member_since('Sett11'))