validate_number=lambda s:['Plenty more fish in the sea','In with a chance'][bool(__import__('re').match(r'^(0|\+44)7([\d-]){9,9}$',s.replace('-','')))]

print(validate_number('87454876120'))
print(validate_number('+447454876120'))