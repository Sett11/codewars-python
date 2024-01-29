is_leap=lambda y:[1==2,1==1][(y%4==0 and y%100!=0) or y%400==0]

print(is_leap(2024))