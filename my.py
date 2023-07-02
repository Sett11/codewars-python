def area_code(s):
    return s[s.index('(')+1:s.index(')')]

print(area_code("The supplier's phone number is (555) 867-5309"))