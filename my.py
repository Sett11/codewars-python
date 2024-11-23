from math import factorial as f

def count_the_ways(a):
    n,m=len(a)//2,len(a[0])//2
    return f(n+m)//(f(n)*f(m))*4 if (n and m) else 2 if (n or m) else 1

print(count_the_ways(['X']))
print(count_the_ways(['M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']))
print(count_the_ways([
['E','D','E'],
['D','C','D'],
['C','B','C'],
['B','A','B'],
['C','B','C'],
['D','C','D'],
['E','D','E']
]))
print(count_the_ways([
            ['E','I','N','E','R','N','H','O','J','S','J','O','H','N','R','E','N','I','E'],
            ['I','N','E','R','N','H','O','J','S','E','S','J','O','H','N','R','E','N','I'],
            ['N','E','R','N','H','O','J','S','E','I','E','S','J','O','H','N','R','E','N'],
            ['E','R','N','H','O','J','S','E','I','L','I','E','S','J','O','H','N','R','E'],
            ['R','N','H','O','J','S','E','I','L','E','L','I','E','S','J','O','H','N','R'],
            ['N','H','O','J','S','E','I','L','E','R','E','L','I','E','S','J','O','H','N'],
            ['H','O','J','S','E','I','L','E','R','E','R','E','L','I','E','S','J','O','H'],
            ['O','J','S','E','I','L','E','R','E','H','E','R','E','L','I','E','S','J','O'],
            ['H','O','J','S','E','I','L','E','R','E','R','E','L','I','E','S','J','O','H'],
            ['N','H','O','J','S','E','I','L','E','R','E','L','I','E','S','J','O','H','N'],
            ['R','N','H','O','J','S','E','I','L','E','L','I','E','S','J','O','H','N','R'],
            ['E','R','N','H','O','J','S','E','I','L','I','E','S','J','O','H','N','R','E'],
            ['N','E','R','N','H','O','J','S','E','I','E','S','J','O','H','N','R','E','N'],
            ['I','N','E','R','N','H','O','J','S','E','S','J','O','H','N','R','E','N','I'],
            ['E','I','N','E','R','N','H','O','J','S','J','O','H','N','R','E','N','I','E']
        ]))