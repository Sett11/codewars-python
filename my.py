from collections import Counter

def what_list_am_i_on(a):
    s='bfkgsn'
    c=Counter(list(map(lambda e:1 if e[0] in s[:3] else 2,filter(lambda e:e[0] in s,a))))
    return 'nice' if c[2]>c[1] else 'naughty'

print(what_list_am_i_on(['broke someone\'s window', 'fought over a toaster', 'killed a bug']))
print(what_list_am_i_on(['got someone a new car', 'saved a man from drowning', 'never got into a fight']))
print(what_list_am_i_on(['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']))