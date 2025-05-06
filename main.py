def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    # Переводим температуру из °C в K
    temp_kelvin = temp + 273.15
    
    # Рассчитываем количество вещества для каждого газа (в молях)
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    
    # Суммарное количество вещества
    n_total = n1 + n2
    
    # Газовая постоянная R
    R = 0.082  # dm³·atm·K⁻¹·mol⁻¹
    
    # Рассчитываем общее давление
    total_pressure = (n_total * R * temp_kelvin) / volume
    
    return total_pressure