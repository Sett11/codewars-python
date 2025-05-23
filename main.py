def is_valid(positions):
    # Проверяем, что король находится между двумя ладьями
    rook_indices = [i for i, piece in enumerate(positions) if piece == 'R']
    king_index = positions.index('K')
    if not (rook_indices[0] < king_index < rook_indices[1]):
        return False
    # Проверяем, что слоны на клетках разного цвета
    bishop_indices = [i for i, piece in enumerate(positions) if piece == 'B']
    if (bishop_indices[0] % 2) == (bishop_indices[1] % 2):
        return False
    return True