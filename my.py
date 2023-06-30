from typing import List,Tuple

def locate_entrance(o:List[str])->Tuple[int,int]:
    o=[i.rstrip() for i in o]
    if '.' in o[0]:
        return (o[0].index('.'),0)
    if '.' in o[-1]:
        return (o[-1].index('.'), len(o)-1)
    for j,i in enumerate(o):
        if i[0]=='.':
            return (0,j)
        if i[len(i)-1]=='.':
            return (len(i)-1,j)
    i=0
    while i<len(o):
        j=0
        while j<len(o[i]):
            if o[i][j]=='.':
                if o[i][j-1]=='#' and o[i][j+1]=='#':
                    if j>len(o[i-1])-1 or j>len(o[i+1])-1:
                        return (j,i)
                    if j<len(o[i+1])-1 and o[i+1][j]==' ' or j<len(o[i-1])-1 and o[i-1][j]==' ':
                        return (j,i)
                if o[i][j-1]==' ' or j==len(o[i])-1:
                    return (j,i)
            j+=1
        i+=1

print(locate_entrance(['####',
                       '#..###',
                       '#....#',
                       '#....#',
                       '######.#....##',
                       '#............#',
                       '##########...#',
                       '#...#',
                       '#...#',
                       '#...#',
                       '#...#',
                       '#...#',
                       '#...#',
                       '#...#',
                       '#####']))
print(locate_entrance([' #####',
                       ' #...#',
                       ' ....#',
                       ' #...#',
                       '##...#',
                       '#....#',
                       '######']))
print(locate_entrance(['##############  ',
                       '#............#  ',
                       '#............###',
                       '###.#####......#',
                       '        #......#',
                       '        ##.....#',
                       '         #.....#',
                       '         #.....#',
                       '         #.....#',
                       '         #######']))