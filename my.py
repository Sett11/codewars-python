def valid_card(s):
    return not sum(map(lambda j:sum(map(int,str(int(j[1])*2))) if j[0]&1 else int(j[1]),enumerate(filter(lambda x:x.isdigit(),list(s[::-1])))))%10

print(valid_card("5457 6238 9823 4311"))
print(valid_card("5457 6238 9323 4311"))