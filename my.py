cache=set()

def hand_out_gift(s):
    if s in cache:
        raise()
    cache.add(s)

print(hand_out_gift('peter'))
print(hand_out_gift('mary'))
print(hand_out_gift('peter'))