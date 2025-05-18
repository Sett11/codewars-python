def movie_times(open, close, length):
    showtimes = []
    current_hour = open
    current_min = 0
    
    # Если кинотеатр закрывается раньше, чем открывается (например, работает ночью)
    if close <= open:
        close += 24
    
    while True:
        # Проверяем, что фильм успеет закончиться до закрытия
        end_hour = current_hour + (current_min + length) // 60
        end_min = (current_min + length) % 60
        
        if end_hour > close or (end_hour == close and end_min > 0):
            break
        
        # Добавляем текущее время в список
        showtimes.append((current_hour % 24, current_min))
        
        # Добавляем 15 минут для перерыва
        current_min += length + 15
        current_hour += current_min // 60
        current_min = current_min % 60
    
    return showtimes