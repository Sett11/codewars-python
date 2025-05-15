def painted_faces(length, n):
    if length == 1:
        return 1 if n == 6 else 0
    if n == 0:
        return (length - 2) ** 3 if length >= 2 else 0
    elif n == 1:
        return 6 * (length - 2) ** 2 if length >= 2 else 0
    elif n == 2:
        return 12 * (length - 2) if length >= 2 else 0
    elif n == 3:
        return 8 if length >= 2 else 0
    else:
        return 0