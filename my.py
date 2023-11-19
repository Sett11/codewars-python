def computer_to_phone(s):
    return s.translate(str.maketrans('789456123','123456789'))


print(computer_to_phone('789'))