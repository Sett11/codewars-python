import re
def guess_my_number(s,n='123-451-2345'):
    return re.sub(r'[^{}-]'.format(s),'#',n)

print(guess_my_number('01234'))