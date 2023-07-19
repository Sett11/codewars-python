from decimal import Decimal,ROUND_HALF_UP

def round_by_2_decimal_places(n):
    return Decimal(n).quantize(Decimal('1.00'),ROUND_HALF_UP)

print(round_by_2_decimal_places(Decimal('2')))
print(round_by_2_decimal_places(Decimal('64.005')))