take_umbrella=lambda a,b:a=='rainy' or (a=='cloudy' and b>.2) or b>.5

print(take_umbrella('sunny', 0.40))