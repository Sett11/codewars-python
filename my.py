def is_infinite_process(a,b):
    return True if ((a&1 and b%2==0) or (b&1 and a%2==0)) else False if a<=b else True