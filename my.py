who_took_the_car_key=lambda a:''.join([chr(int(i,2)) for i in a])

print(who_took_the_car_key(['01000001', '01101100', '01100101', '01111000', '01100001', '01101110',
             '01100100', '01100101', '01110010']))