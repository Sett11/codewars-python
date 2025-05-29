def validate_base(num: str, base: int) -> bool:
    if base < 2 or base > 36:
        return False
    
    max_digit_value = base - 1
    valid_digits = set()
    
    # Добавляем цифры от 0 до 9, если они меньше base
    for digit in range(0, min(10, base)):
        valid_digits.add(str(digit))
    
    # Добавляем буквы A-Z, если base > 10
    if base > 10:
        for letter_ord in range(ord('A'), ord('A') + (max_digit_value - 9)):
            valid_digits.add(chr(letter_ord))
    
    # Проверяем каждый символ в num
    for char in num:
        if char not in valid_digits:
            return False
    
    return True