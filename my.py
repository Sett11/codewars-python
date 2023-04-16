def string_to_int_list(s):
    return list(map(int,filter(lambda e:e,s.split(','))))

print(string_to_int_list("21,,12,23,34,45"))