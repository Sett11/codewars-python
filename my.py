def head_smash(a):
    if(isinstance(a,int)):return "This isn't the gym!!"
    return  'Gym is empty' if len(a)==0 else list(map(lambda e:e.replace('O',' '),a))

print(head_smash([
'*****************************************',
'**  _O_   *   _O_   *   _O_   *   _O_  **',
'** /(.)J  *  C(.)J  *  /(.)J  *  C(.)J **',
'** _| |_  *  _| |_  *  _( )_  *  _( )_ *']))