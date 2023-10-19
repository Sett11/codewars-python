def solution(m):
    try:return next(bool(i) for i in m if '>' in i and 'x' in i and i.index('>')<i.index('x'))
    except:return False

print(solution([
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', '>', ' ', 'x'],
  [' ', ' ', '', ' ', ' ']
]))
print(solution([
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', '>', ' ', ' '],
  [' ', ' ', ' ', ' ', 'x'],
  [' ', ' ', '', ' ', ' ']
]))