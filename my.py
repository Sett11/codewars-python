from random import choice
a,b=['2','3','4','5','6','7','8','9','10','J','Q','K','A'],['H','D','S','C']
c,d,pl=choice(a),choice(b),input('Choose').lower()
if pl=='red' and d in ['H','D']:
  print(f'Wow {c} {d}')
elif pl=='black' and d in ['S','C']:
  print(f'Wow {c} {d}')
else:
  print('Oh')