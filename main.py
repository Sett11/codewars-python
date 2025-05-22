import math

def solution(force1, force2, theta):
    # Переводим угол theta из градусов в радианы
    theta_rad = math.radians(theta)
    # Вычисляем компоненты результирующей силы
    R_x = force1 + force2 * math.cos(theta_rad)
    R_y = force2 * math.sin(theta_rad)
    # Вычисляем модуль результирующей силы
    R = math.sqrt(R_x**2 + R_y**2)
    # Вычисляем угол phi в радианах, затем переводим в градусы
    if R_x == 0:
        if R_y > 0:
            phi_rad = math.pi / 2
        elif R_y < 0:
            phi_rad = -math.pi / 2
        else:
            phi_rad = 0  # Если R_y тоже 0, угол не определён, можно вернуть 0
    else:
        phi_rad = math.atan2(R_y, R_x)
    phi_deg = math.degrees(phi_rad)

    # Возвращаем результат с округлением до разумного количества знаков (например, 2)
    return [R, phi_deg]