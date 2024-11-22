circle_slash=lambda n:(n-(1<<31-bin(n)[2:].rjust(32,'0').find('1')))*2+1

print(circle_slash(219))