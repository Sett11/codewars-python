from urllib import parse

def generate_link(s):
    return 'http://www.codewars.com/users/'+parse.quote(s)

print(generate_link('matt c'))