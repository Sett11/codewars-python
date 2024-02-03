def get_new_notes(s,b):
    n=(s-sum(b))//5
    return 0 if n<0 else n

print(get_new_notes(10000,[1800, 500, 1200, 655, 150]))