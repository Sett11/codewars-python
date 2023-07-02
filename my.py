def greet_jedi(a,l):
    return f'Greetings, master {(l[0].upper()+l[1:3]+a[0].upper()+a[1])}'

print(greet_jedi('Beyonce','Knowles'))