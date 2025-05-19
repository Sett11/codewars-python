def brightest(colors):
    max_brightness = -1
    brightest_color = ""
    
    for color in colors:
        # Извлекаем компоненты R, G, B
        r = color[1:3]
        g = color[3:5]
        b = color[5:7]
        
        # Конвертируем из hex в int
        r_int = int(r, 16)
        g_int = int(g, 16)
        b_int = int(b, 16)
        
        # Находим максимальное значение компонента
        current_brightness = max(r_int, g_int, b_int)
        
        # Сравниваем с текущей максимальной яркостью
        if current_brightness > max_brightness:
            max_brightness = current_brightness
            brightest_color = color
        elif current_brightness == max_brightness:
            # Если яркость такая же, оставляем первый встретившийся цвет
            pass
    
    return brightest_color