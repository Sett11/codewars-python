import re
def filter_numbers(s):
    return re.sub(r'\d+','',s)

print(filter_numbers("aa1 bb2cc3dd"))