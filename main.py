def solution(arr_val, arr_unit):
    # Гравитационная постоянная
    G = 6.67e-11  # N⋅kg^-2⋅m^2
    
    # Массы и расстояние из arr_val
    m1_val, m2_val, r_val = arr_val
    
    # Единицы из arr_unit
    m1_unit, m2_unit, r_unit = arr_unit
    
    # Конвертация массы obj1 в кг
    m1_kg = convert_mass_to_kg(m1_val, m1_unit)
    
    # Конвертация массы obj2 в кг
    m2_kg = convert_mass_to_kg(m2_val, m2_unit)
    
    # Конвертация расстояния в метры
    r_m = convert_distance_to_meters(r_val, r_unit)
    
    # Расчет силы
    force = G * (m1_kg * m2_kg) / (r_m ** 2)
    
    return force

def convert_mass_to_kg(value, unit):
    # Конвертирует массу в килограммы
    if unit == 'kg':
        return value
    elif unit == 'g':
        return value * 0.001
    elif unit == 'mg':
        return value * 1e-6
    elif unit == 'μg':
        return value * 1e-9
    elif unit == 'lb':
        return value * 0.453592
    else:
        raise ValueError(f"Unknown mass unit: {unit}")

def convert_distance_to_meters(value, unit):
    # Конвертирует расстояние в метры
    if unit == 'm':
        return value
    elif unit == 'cm':
        return value * 0.01
    elif unit == 'mm':
        return value * 0.001
    elif unit == 'μm':
        return value * 1e-6
    elif unit == 'ft':
        return value * 0.3048
    else:
        raise ValueError(f"Unknown distance unit: {unit}")